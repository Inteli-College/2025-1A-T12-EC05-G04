from app.Controllers.ListaController import ListaController
from app.Models.InstrucaoRoboModel import InstrucaoRobo, db
from app.Models.MontagemModel import Montagem
from app.Models.LoteModel import Lote
from app.Models.ListaModel import Lista
from app.Websockets import send_message
from flask import jsonify
import json
from app.QueueManager import QueueManager
from app.datetime import datetime_sp_string as dt

# Comentário bacana

queue_inst = QueueManager("instrucao")
lista = ListaController()

class RoboController:

    def __init__(self):
        pass


    def iniciarMontagem(self, data):
        """Recebe uma nova mensagem e lista"""

        id_montagem = data['id']
        # Pega o objeto montagem
        
        print("Montagem iniciada: ", id_montagem)
        
        montagem = Montagem.query.filter_by(id=id_montagem).first()

        if montagem.status == 2:
            return jsonify({
                "message": f'Essa montagem já foi finalizada.... IdMontagem: {id_montagem}',
                "code": 409
            })

        id_lista = montagem.id_lista
        lista = Lista.query.filter_by(id=id_lista).first()
 
        query_louca = (db.session.query(Lista.id_remedio).join(Montagem, Lista.id == Montagem.id_lista).filter(Montagem.id == id_montagem).first())
        
        id_remedio = query_louca.id_remedio
        first_instrucao = InstrucaoRobo.query.filter_by(id_remedio=id_remedio).first()

        listas_mesma_fita = Lista.query.filter_by(id_fita=lista.id_fita).all()
        ids_remedio = [lista.id_remedio for lista in listas_mesma_fita]
        instrucoes = InstrucaoRobo.query.filter(InstrucaoRobo.id_remedio.in_(ids_remedio)).all()
        
        if not listas_mesma_fita:
            return jsonify({
                "message": f'Erro ao buscar as listas na mesma fita...',
                'code': 404
            }), 404

        if not ids_remedio:
            return jsonify({
                "message": f'Erro ao buscar o ids dos remedios...',
                'code': 404
            }), 404   

        if not instrucoes:
            return jsonify({
                "message": f'Erro ao buscar o instruções...',
                'code': 404
            }), 404         
 
        if not id_remedio:
            return jsonify({
                "message": f'Erro ao buscar o id remedio...',
                'code': 404
            }), 404


        if instrucoes:

            for lista in listas_mesma_fita:
                # Pega a montagem relacionada à lista
                montagem = Montagem.query.filter_by(id_lista=lista.id).first()
                if not montagem:
                    continue  # pula se não houver montagem relacionada
                if montagem.id == id_montagem:
                    continue

                # Pega a instrução relacionada ao id_remedio
                instrucao = InstrucaoRobo.query.filter_by(id_remedio=lista.id_remedio).first()
                if not instrucao:
                    continue  # pula se não houver instrução

                # Cria o pacote de dados e envia para a fila
                data = {
                    "instrucao": instrucao.instrucao,
                    "id_montagem": montagem.id  # id_montagem de cada remédio
                }
                queue_inst.add_message(data)
                print("AQUIIII ESTÁ AS PRÓXIMAS INSTRUÇÕESSS", data)

            instrucao_ws = send_message("instrucao", {"instrucao":first_instrucao.instrucao, "id_montagem": id_montagem})

            if instrucao_ws['status'] != "sucess":
                print("Algo deu errado ao enviar a mensagem...")
                return jsonify({
                    "message": instrucao_ws["message"]
                }), 500
            
            print("Mensagem enviada com sucesso!", instrucao_ws)

            montagem = db.session.query(Montagem).filter_by(id=id_montagem).first()

            if montagem:
                try:
                    montagem.status = 1  # Atualiza o campo `status`
                    db.session.commit()  # Confirma a alteração no banco

                    return jsonify({
                        "id": id_montagem,
                        "montagem_status": 1,
                        "id_remedio": id_remedio,
                        "id_instrucao": first_instrucao.id,
                        "montagem": True
                    }), 201
                

                except Exception as e:
                    db.session.rollback()
                    return {
                        'message': f'Erro ao atualizar Montagem: {e}',
                        'code': 500
                    }, 500                    

                
            return jsonify({
                'message': f"Montagem não encontrada no banco de dados...",
                'code':404
            }), 404

        
        else:
            return jsonify({
                "message": "Nenhuma instrução encontrada..."
            }), 404
