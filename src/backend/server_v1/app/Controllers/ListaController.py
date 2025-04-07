from flask import request, jsonify
from app.Models.PacienteModel import Paciente
from app.Models.ListaModel import Lista
from app.Models.MontagemModel import Montagem
from app.Models.LoteModel import Lote
from app.Schemas.Schemas import ListaSchema, MontagemSchema
from app.Models.UsuarioModel import Usuario
from app import db
import uuid
import logging
logger = logging.getLogger(__name__)


from app.datetime import datetime_sp_string

montagem_schema = MontagemSchema()

lista_schema = ListaSchema()
listas_schema = ListaSchema(many=True)

def gerar_novo_id_fita():
    return str(uuid.uuid4())


class ListaController:

    def __init__(self):
        pass

    def createLista(self, dados_nova_lista):
        try:
            nova_lista = lista_schema.load(dados_nova_lista, session=db.session)
            db.session.add(nova_lista)
            db.session.commit()
            # Retorne a instância (você pode usar o dump se preferir)
            return nova_lista, 201
        except Exception as e:
            db.session.rollback()
            return {"erro ao adicionar lista": str(e)}, 500
        
    def createListaPorIdPaciente(self, paciente, remedios):
        """
        Cria um registro na tabela 'lista' com os campos id_paciente, id_fita, id_remedio e quantidade.
        """
        try:

            novo_id_fita = gerar_novo_id_fita()  # Criamos essa função logo abaixo
            print(novo_id_fita)
            for r in remedios:
                remedio_id = r.get("remedioID") or r.get("id_remedio")
                quantidade = r.get("quantidade")
                if remedio_id and quantidade:
                    nova_lista = Lista(
                        id_paciente=paciente.id,
                        id_fita=novo_id_fita,  # Usa o mesmo id_fita, que é o id do registro master
                        id_remedio=remedio_id,
                        quantidade=quantidade
                    )
                    db.session.add(nova_lista)
            db.session.commit()
            if not nova_lista:
                return {"erro": "Nenhum remédio válido foi informado."}, 400

            return nova_lista, 201
        except Exception as e:
            db.session.rollback()
            return {"erro ao adicionar lista": str(e)}, 500

    def getRemediosDisponiveis(self):
        try:
            # Consulta todos os remédios com quantidade > 0
            remedios = Lote.query.filter(Lote.quantidade > 0).all()

            lista = [
                {
                    "id": r.id,
                    "remedio": r.remedio,
                    "dose": r.dose,
                    "quantidade": r.quantidade,
                    "validade": r.validade
                }
                for r in remedios
            ]
            return lista, 200
        except Exception as e:
            return {"erro": str(e)}, 500

    def createListaAndMontagem(self, dados_nova_lista):
        lista_criada, status_code = self.createLista(dados_nova_lista)
        if status_code != 201:
            return lista_criada, status_code
        dados_nova_montagem = {
            'id_lista': lista_criada.id,
            'id_usuario': None,
            'datetime': datetime_sp_string,
            'status': 0
        }
        try:
            nova_montagem = montagem_schema.load(dados_nova_montagem, session=db.session)
            db.session.add(nova_montagem)
            db.session.commit()
            # Retorne um dicionário serializável, usando dump
            return montagem_schema.dump(nova_montagem), 201, lista_criada
        except Exception as e:
            db.session.rollback()
            return {"erro ao adicionar montagem": str(e)}, 500

    def createFromFormulario(self, emergencia_lista):
        try:
            nome = emergencia_lista.get("nomePaciente")
            hc = emergencia_lista.get("hc")
            leito = emergencia_lista.get("leito")
            enfermeiro_id = emergencia_lista.get("enfermeiro_id")
            remedios = emergencia_lista.get("remedios", [])

            # 1. Validação do paciente
            paciente = Paciente.query.filter_by(nome=nome, HC=hc, Leito=leito).first()
            if not paciente:
                return {"erro": "Paciente não encontrado com os dados fornecidos."}, 400

            # 2. Criação da nova lista para esse paciente
            lista_criada, status_code = self.createListaPorIdPaciente(paciente, remedios)
            if status_code != 201:
                return lista_criada, status_code  # erro já tratado no método

            # 5. Criação da montagem associada ao master da lista e ao enfermeiro
            dados_nova_montagem = {
                'id_lista': lista_criada.id,
                'id_usuario': enfermeiro_id,
                'datetime': datetime_sp_string,
                'status': 0
            }
            nova_montagem = montagem_schema.load(dados_nova_montagem, session=db.session)
            db.session.add(nova_montagem)
            db.session.commit()

            remedios_deletados, status_code = self.deleteRemedioForms(remedios)
            if status_code != 201:
                return remedios_deletados, status_code  # erro já tratado no método
            
            return montagem_schema.dump(nova_montagem), 201

        except Exception as e:
            db.session.rollback()
            return {"erro geral": str(e)}, 500

    def deleteRemedioForms(self, remedios):
        try:
            for r in remedios:
                remedio_id = r.get("remedioID") or r.get("id_remedio")
                if remedio_id:
                    remedio = Montagem.query.get_or_404(remedio_id)
                    db.session.delete(remedio)
                    db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"erro ao deletar remédios selecionados": str(e)}, 500