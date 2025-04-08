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

class WsIntegracaoController:
    def __init__(self):
        pass

    def roboStatus(self):
        data = queue_rs.get_message()

        acao = data['acao']
        percentage = data['percentage']
        id_montagem = data['id_montagem']
        
        # Pega o objeto montagem
        montagem = Montagem.query.filter_by(id=id_montagem).first()
        if not montagem:
            return 0, jsonify({'message': "Montagem inexistente", 'code': 404})

        # Id Lista a partir de montagem
        id_lista = montagem.id_lista
        lista = Lista.query.filter_by(id=id_lista).first()
        if not lista:
            return 0, jsonify({'message': "Lista inexistente para a montagem informada", 'code': 404})

        # Pega o objeto Paciente
        paciente = Paciente.query.filter_by(id=lista.id_paciente).first()
        if not paciente:
            return 0, jsonify({'message': "Paciente não encontrado", 'code': 404})

        # Pega o objeto Lote (Remédio)
        lote = Lote.query.filter_by(id=lista.id_remedio).first()
        if not lote:
            return 0, jsonify({'message': "Lote (remédio) não encontrado", 'code': 404})

        response = {
            "PacienteId": paciente.id,
            "Paciente": {
                "nome": paciente.nome,
                "hc": paciente.HC,
                "leito": paciente.Leito
            },
            "Medicamentos": [
                { "nome": lote.remedio, "quantidade": lista.quantidade }
            ],
            "Logs": [
                { "NomeRemedio": lote.remedio, "Porcentagem": percentage }
            ],
            "StatusMontagem": 1
        }
        return 1, jsonify(response)

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
                queue_qr.add_message(data)
                return 0, jsonify({
                    'message': "Algo deu errado ao aplicar mudanças no banco de dados",
                    'code': 500
                })

        return jsonify({
            'message': "Montagem inexistente no banco de dados?",
            'code': 404
        })   

    def errorStatus(self):

        data = queue_es.get_message()

        message = data['message']
        






