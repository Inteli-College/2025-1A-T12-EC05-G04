from app.Models.MontagemModel import Montagem, db
from app.Models.ListaModel import Lista
from app.Models.LoteModel import Lote
from app.Models.PacienteModel import Paciente
from app.Models.ErroMontagemModel import ErroMontagem
from flask import jsonify
from app.QueueManager import QueueRoboStatus, QueueErrorStatus, QueueQrCode

queue_rs = QueueRoboStatus
queue_qr = QueueQrCode
queue_es = QueueErrorStatus

def attStatusMontagem(id_m, result):
    montagem = Montagem.query.filter_by(id=id_m).first()
    montagem.status = result

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

        acao = data['acao']
        percentage = data['percentage']
        id_montagem = data['id_montagem']
        
        if percentage == 0:
        # Pega o objeto montagem
            montagem = Montagem.query.filter_by(id=id_montagem).first()

            if montagem:
                # Id Lista a partir de montagem
                id_lista = montagem.id_lista

                # Pega o objeto Lista
                lista = Lista.query.filter_by(id=id_lista).first()

                # Pega o objeto Paciente
                paciente = Paciente.query.filter_by(id=lista.id_paciente).first()

                # Pega o objeto Lote (Remédio)
                lote = Lote.query.filter_by(id=lista.id_remedio).first()

                id_fita = lista.id_fita

                listas = Lista.query.filter_by(id_fita=id_fita).all()

                attStatusMontagem(id_montagem, 1)


                return "montagem_remedio", jsonify({
                    "PacienteId": paciente.id,
                    "Paciente": {
                        "nome": paciente.nome,
                        "hc": paciente.HC,
                        "leito": paciente.Leito
                    },
                    "Medicamentos": [
                        { "nome": Lote.query.filter_by(id=lis.id_remedio).remedio }
                        for lis in listas
                    ],
                    "StatusMontagem": 1,
                    "Topico": "Start"

                })

            
            else:
                return "montagem_remedio", jsonify({
                    'message': "Montagem inexistente",
                    'code': 404
                })
            
        elif percentage == 100:
            attStatusMontagem(id_montagem, 2)

            return "robo_status_fe", jsonify({
                "NomeRemedio": lote.remedio,
                "Porcentagem": percentage,
                "StatusMontagem": 2,
                "Topico": "Finish"              
            })
            
        else:
            # Id Lista a partir de montagem
            id_lista = montagem.id_lista

            # Pega o objeto Lista
            lista = Lista.query.filter_by(id=id_lista).first()

            # Pega o objeto Lote (Remédio)
            lote = Lote.query.filter_by(id=lista.id_remedio).first()


            return "robo_status_fe", jsonify({
                "NomeRemedio": lote.remedio,
                "Porcentagem": percentage,
                "Topico": "Porcentagem"              
            })


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






