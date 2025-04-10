from app.Models.MontagemModel import Montagem, db
from app.Models.ListaModel import Lista
from app.Models.LoteModel import Lote
from app.Models.PacienteModel import Paciente
from app.Models.ErroMontagemModel import ErroMontagem
from app.Models.LogsModel import Logs
from flask import jsonify
from app.QueueManager import QueueManager
import json
from app.datetime import datetime_sp_string as dt
import re


queue_rs = QueueManager("robo_status")
queue_qr = QueueManager("qr_code")
queue_es = QueueManager("error_status")


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
        print("Esse é o dado bacana",data)
        if type(data) == str:
            data = json.loads(data)
        acao = data['acao']
        percentage = data['percentage']
        id_montagem = data['id_montagem']
        # Primeira consulta: monta (Montagem, Lista, Lote) para um id_montagem específico
        result = (
            db.session.query(Montagem, Lista, Lote)
            .join(Lista, Montagem.id_lista == Lista.id)
            .join(Lote, Lista.id_remedio == Lote.id)
            .filter(Montagem.id == id_montagem)
            .first()
        )
        if not result:
            return "montagem_remedio", {
                'message': "Montagem inexistente",
                'code': 404
            }
        # Desempacota a tupla retornada
        montagem, lista, lote = result
        if percentage == 0.125:
            if montagem:
                # Pega o objeto Paciente
                paciente = Paciente.query.filter_by(id=lista.id_paciente).first()
                # Pega o id da Fita
                id_fita = lista.id_fita
                listas = (
                        db.session.query(Lista, Lote)
                        .join(Lote, Lista.id_remedio == Lote.id)
                        .filter(Lista.id_fita == id_fita)
                        .all()
                    )
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
        elif percentage == 1.00:
            attStatusMontagem(id_montagem, 2)
            # Obtém o id_fita da lista associada para agrupar as montagens
            id_fita = lista.id_fita
            # Consulta todas as montagens associadas ao mesmo id_fita
            group_results = (
                db.session.query(Montagem)
                .join(Lista, Montagem.id_lista == Lista.id)
                .filter(Lista.id_fita == id_fita)
                .all()
            )
            # Se todas as montagens do grupo estiverem finalizadas (status == 2), atualiza para 1
            if all(montagem.status == 2 for montagem in group_results):
                for m in group_results:
                    m.status = 1
                try:
                    db.session.commit()
                    print("Todas as montagens da fita foram finalizadas e o status atualizado para 1.")
                    # Retorna payload indicando que a fita foi finalizada (status 1)
                    return {
                        "NomeRemedio": lote.remedio,
                        "Porcentagem": percentage,
                        "IdMontagem": id_montagem,
                        "StatusMontagem": 1,
                        "Topico": "Finish"
                    }
                except Exception as e:
                    db.session.rollback()
                    return {
                        "message": f"Erro ao atualizar status da fita: {e}",
                        "code": 500
                    }
            else:
                # Caso contrário, retorna os dados individuais com status 2
                return {
                    "NomeRemedio": lote.remedio,
                    "Porcentagem": percentage,
                    "IdMontagem": id_montagem,
                    "StatusMontagem": 2,
                    "Topico": "Finish"
                }
        else:
            # Para casos intermediários (Ongoing)
            id_lista = montagem.id_lista
            MedicamentoResult = (
                db.session.query(Lista, Lote)
                .join(Lista, Lote.id == Lista.id_remedio)
                .filter(Lista.id == id_lista)
                .first()
            )
            if MedicamentoResult:
                lista_obj, lote_obj = MedicamentoResult
                return {
                    "NomeRemedio": lote_obj.remedio,
                    "Porcentagem": percentage,
                    "IdMontagem": id_montagem,
                    "Topico": "Ongoing"
                }
            else:
                return {
                    "message": "Dados incompletos para atualização de Ongoing",
                    "code": 404
                }
    def qrCode(self):
        data = queue_qr.get_message()
        if type(data) == str:
            data = json.loads(data)
        qr = str(data['qr'])
        qr_codigo = qr.split(":")[1]
        id_montagem = data['id_montagem']
        # Pega o objeto montagem
        montagem = Montagem.query.filter_by(id=id_montagem).first()
        id_lista = montagem.id_lista
        lista = Lista.query.filter_by(id=id_lista).first()
        id_remedio = lista.id_remedio
        lote = Lote.query.filter_by(id=id_remedio).first()
        print("Codigo QR PAPAI:", qr_codigo)
        if montagem:
            real_qr = lote.codigo
            print("REAL QR PAPAI:", real_qr)
            if qr_codigo == real_qr:
                print("É o mesmo qr code papai", id_montagem, id_remedio, dt)
                new = Logs(id_montagem=id_montagem, id_remedio=id_remedio, datetime=dt)
                try:
                    db.session.add(new)
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
            return {
                "IdMontagem": id_montagem,
                "Message": message
            }
        except Exception as e:
            return jsonify({
                'message': f"Erro ao criar montagem {e}",
                'code': 500
            })

