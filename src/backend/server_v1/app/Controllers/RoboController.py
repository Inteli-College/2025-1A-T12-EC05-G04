from app.Controllers.ListaController import ListaController
from app.Models.InstrucaoRoboModel import InstrucaoRobo, db
from app.Models.MontagemModel import Montagem
from app.Websockets import send_message
from flask import jsonify


lista = ListaController()

class RoboController:

    def __init__(self):
        pass


    def iniciarMontagem(self, data):
        """Recebe uma nova mensagem e lista"""
        
        new_montagem, code, new_lista = lista.createListaAndMontagem(data)

        if code != 201:
            print("Robo Controller: Algo deu errado...")
            return jsonify({
                "message": "Erro ao criar montagem",
                "montagem": new_montagem,
                "lista": new_lista
            }), code

        id_montagem = new_montagem['id']
        id_remedio = int(new_lista.id_remedio)

        try:
            instrucaorobo = db.session.query(InstrucaoRobo).filter_by(id_remedio=id_remedio).first()


        except Exception as e:
            db.session.rollback()
            return jsonify({
                'message': f'Erro ao buscar a Instrução: {str(e)}'
            }), 500

        if instrucaorobo:
            vivo = send_message("conectado", "Ta vivo?")

            if vivo.get("status") != "sucess":
                print("Cliente não conectado...")
                return jsonify({
                    "message": "Cliente desconectado..."
                }), 500

            instrucao_ws = send_message("instrucao", {"instrucao":instrucaorobo.instrucao, "id_montagem": id_montagem})

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
                        "id_instrucao": instrucaorobo.id,
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


    def pararMontagem(self):
        pass

    def deletarMontagem(self):
        pass

