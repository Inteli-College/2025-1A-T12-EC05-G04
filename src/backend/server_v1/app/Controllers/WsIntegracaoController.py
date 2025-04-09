from app.Models.MontagemModel import Montagem, db
from app.Models.ListaModel import Lista
from app.Models.LoteModel import Lote
from app.Models.PacienteModel import Paciente
from app.Models.ErroMontagemModel import ErroMontagem
from flask import jsonify

from sqlalchemy.orm import aliased
from app.QueueManager import QueueRoboStatus, QueueErrorStatus, QueueQrCode
import json
from app.datetime import datetime_sp_string as dt

queue_rs = QueueRoboStatus()
queue_qr = QueueQrCode()
queue_es = QueueErrorStatus()

def attStatusMontagem(id_m, result):
    montagem = Montagem.query.filter_by(id=id_m).first()
    montagem.status = result
    montagem.datetime = dt

    try:
        db.session.commit()
        print("Status da montagem alterado com sucesso no banco! :D")

    except Exception as e:
        return jsonify({
            'message': f"Algo deu errado ao aplicar mudanças no banco de dados {e}",
            'code': 500
        })
    


class WsIntegracaoController:
    def __init__(self):
        pass


    def montagemRemedio(self):
        data = queue_rs.get_message()

        if type(data) == str:
            data = json.loads(data)

        acao = data['acao']
        percentage = data['percentage']
        id_montagem = data['id_montagem']

        result = db.session.query(Montagem, Lista, Lote)\
            .join(Lista, Montagem.id_lista == Lista.id)\
            .join(Lote, Lista.id_remedio == Lote.id)\
            .filter(Montagem.id == id_montagem)\
            .first()

        if result:
            montagem, lista, lote = result    
        
        if percentage == 0:

            if montagem:

                # Pega o id da Fita
                id_fita = lista.id_fita

                listas = (
                        db.session.query(Paciente, Lista, Lote)\
                        .join(Lista, Paciente.id == Lista.id_paciente)\
                        .join(Lote, Lista.id_remedio == Lote.id)\
                        .filter(Lista.id_fita == id_fita)\
                        .all()
                    )
                
                if result:
                    # Como o paciente é único para o grupo,
                    # basta pegar o paciente do primeiro registro e as listas de todos os registros
                    paciente, _, _ = result[0]
        
                    # Para construir a lista de listas junto com os remédios, você pode fazer:
                    listas = [{"lista": l, "lote": lot} for (_, l, lot) in result]
                
                attStatusMontagem(id_montagem, 1)

                return {
                    "PacienteId": paciente.id,
                    "Paciente": {
                        "nome": paciente.nome,
                        "hc": paciente.HC,
                        "leito": paciente.Leito
                    },
                    "Medicamentos": [
                        {
                            "nome": lote.remedio,
                            "quantidade": lote.quantidade
                        } for lista, lote in listas
                    ],
                    "StatusMontagem": 1,
                    "Topico": "Start"
                }
            
            else:
                return "montagem_remedio", {
                    'message': "Montagem inexistente",
                    'code': 404
                }
            
        elif percentage == 100:
            attStatusMontagem(id_montagem, 2)

            return {
                # nao ta conseguindo acessar o lote.remeido daqui.
                "NomeRemedio": lote.remedio,
                "Porcentagem": percentage,
                "StatusMontagem": 2,
                "Topico": "Finish"              
            }
            
        else:
            # Id Lista a partir de montagem
            id_lista = montagem.id_lista

            # Pega o objeto Lista
            lista = Lista.query.filter_by(id=id_lista).first()

            # Pega o objeto Lote (Remédio)
            lote = Lote.query.filter_by(id=lista.id_remedio).first()


            return {
                "NomeRemedio": lote.remedio,
                "Porcentagem": percentage,
                "Topico": "Ongoing"              
            }



    def qrCode(self):
        data = queue_qr.get_message()

        result = data['result']
        qr = data['qr']
        id_montagem = data['id_montagem']

        # Pega o objeto montagem
        montagem = Montagem.query.filter_by(id=id_montagem).first()
        lista = Montagem.query.filter_by(id=montagem.id_lista)
        lote = Lote.query.filter_by(id=lista.id_remedio).first()

        if montagem:
            montagem.status = result
            lote.codigo = qr

            try:
                db.session.commit()
                print("Status da montagem alterado com sucesso no banco! :D")

            except Exception as e:

                return jsonify({
                    'message': f"Algo deu errado ao aplicar mudanças no banco de dados {e}",

                    'code': 500
                })

        return jsonify({
            'message': "Montagem inexistente no banco de dados?",
            'code': 404
        })   

    def errorStatus(self):

        data = queue_es.get_message()

        id_montagem = data['id_montagem']
        message = data['message']

        montagem = Montagem.query.filter_by(id=id_montagem).first()

        new = ErroMontagem(id_montagem=id_montagem, mensagem=message)
        try:
            db.session.add(new)
            db.session.commit()

            return jsonify({
                "Montagem": montagem,
                "Message": message
            })
        
        except Exception as e:
            return jsonify({
                'message': f"Erro ao criar montagem {e}",
                'code': 500
            })







