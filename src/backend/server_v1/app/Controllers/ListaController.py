from flask import request, jsonify
from app.Models.PacienteModel import Paciente
from app.Models.ListaModel import Lista
from app.Models.MontagemModel import Montagem
from app.Models.LoteModel import Lote
from app.Schemas.Schemas import ListaSchema, MontagemSchema
from app.Models.UsuarioModel import Usuario
from app import db

from app.datetime import datetime_sp_string

montagem_schema = MontagemSchema()

lista_schema = ListaSchema()
listas_schema = ListaSchema(many=True)

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
        
    def createListaPorIdPaciente(self, paciente):
        try:
            nova_lista = Lista(id_paciente=paciente.id)
            db.session.add(nova_lista)
            db.session.commit()
            # Retorne a instância (você pode usar o dump se preferir)
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
            lista_criada, status_code = self.createListaPorIdPaciente(paciente)
            if status_code != 201:
                return lista_criada, status_code  # erro já tratado no método

            # 3. Inserção dos remédios na lista
            try:
                for r in remedios:
                    if r.get("id_remedio") and r.get("quantidade"):
                        item = Lista(
                            id_paciente=paciente.id,
                            id_remedio=r["id_remedio"],
                            quantidade=r["quantidade"]
                        )
                        db.session.add(item)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {"erro ao registrar remédios": str(e)}, 500

            # 4. Criação da montagem associada à lista e ao enfermeiro
            dados_nova_montagem = {
                'id_lista': lista_criada.id,
                'id_usuario': enfermeiro_id,
                'datetime': datetime_sp_string,
                'status': 0
            }

            try:
                nova_montagem = montagem_schema.load(dados_nova_montagem, session=db.session)
                db.session.add(nova_montagem)
                db.session.commit()
                return montagem_schema.dump(nova_montagem), 201
            except Exception as e:
                db.session.rollback()
                return {"erro ao adicionar montagem": str(e)}, 500

        except Exception as e:
            db.session.rollback()
            return {"erro geral": str(e)}, 500
