from app.Controllers.ListaController import ListaController
from app.Models.InstrucaoRoboModel import InstrucaoRobo, db
from app.Websockets import send_message


lista = ListaController()

class RoboController:

    def __init__(self):
        pass


    def iniciarMontagem(self, data):
        """Recebe uma nova mensagem e lista """
        
        new_montagem, code, new_lista = lista.createListaAndMontagem(data)

        if code != 201:
            print("Robo Controller: Algo deu errado...")
            return new_montagem, code, new_lista
        
        else:
            id_montagem = new_montagem['id']
            id_remedio = new_lista['id_remedio']
            instrucaorobo = InstrucaoRobo.query.get(id_remedio)

            if instrucaorobo:
                instrucao = {"Instrução": instrucaorobo.instrucao}
                vivo = send_message("connect", "Ta vivo?")

                if vivo["status"] != "sucess":
                    print("Cliente não conectado...")

                    return {
                        "message": "Cliente desconectado...",
                        "code": 500
                    }, 500

                instrucao_ws = send_message("instrucao", instrucao)
                print("Mensagem enviada com sucesso!", instrucao_ws)
                return {
                    "id": id_montagem,
                    "id_remedio": id_remedio,
                    "id_instrucao": instrucaorobo.id,
                    "montagem": True
                }, 201


    def pararMontagem(self):
        pass

    def deletarMontagem(self):
        pass






                





            




