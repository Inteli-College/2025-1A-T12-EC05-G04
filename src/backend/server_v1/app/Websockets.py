from flask_socketio import SocketIO
from app.QueueManager import QueueErrorStatus, QueueQrCode, QueueRoboStatus
import logging

# Depois mudar a origem da conexão para o do Raspberry
socketio = SocketIO(cors_allowed_origins="*")  

queue_es = QueueErrorStatus
queue_qr = QueueQrCode
queue_rs = QueueRoboStatus

@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("robo_status")
def handle_message(data):
    socketio.emit('message_status', {"message":"Mensagem recebida no servidor no evento robo_status! :D"})
    print(f"Mensagem recebida: {data}")
    queue_rs.add_message(data)  

@socketio.on("qr_code")
def handle_message(data):    
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento qr_code! :D"})
    print(f"Mensagem recebida: {data}")
    queue_qr.add_message(data) 

@socketio.on("error_status")
def handle_message(data):    
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento error_status"})
    print(f"Mensagem recebida: {data}")
    queue_es.add_message(data)  

instrucao = {"tipoAcao":{"0":"1","1":"1","2":"2","3":"1","4":"3","5":"1","6":"1","7":"3"},"valorGrab":{"0":"0","1":"0","2":"0","3":"0","4":"1","5":"0","6":"0","7":"0"},"x":{"0":226.9400024414,"1":354.7524719238,"2":234.8511962891,"3":307.1087646484,"4":"0","5":307.1087646484,"6":338.8617248535,"7":"0"},"y":{"0":-8.8123865128,"1":-72.7444534302,"2":-96.7423095703,"3":-74.8153915405,"4":"0","5":-74.8153915405,"6":-56.0145263672,"7":"0"},"z":{"0":142.8887023926,"1":72.2275466919,"2":61.2597045898,"3":-57.2363128662,"4":"0","5":-57.2363128662,"6":71.1682739258,"7":"0"}}

@socketio.on("instrucao_teste")
def handle_message(data):    
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento error_status"})
    socketio.emit('instrucao', {"instrucao":instrucao, "id_montagem": 3})
    print(f"Mensagem recebida: {data}")
    queue_es.add_message(data)  


@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")

def send_message(event, data):
    """Envia mensagem Websocket"""
    try:
        socketio.emit(event,data)
        return {"status": "sucess", "message": "Mensagem enviada com sucesso! :D"}
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem WebSocket: {e}")
        return {"status": "error", "message": f"Erro ao enviar mensagem: {str(e)}"}

instrucao = '{"tipoAcao":{"0":"1","1":"1","2":"2","3":"1","4":"3","5":"1","6":"1","7":"3"},"valorGrab":{"0":"0","1":"0","2":"0","3":"0","4":"1","5":"0","6":"0","7":"0"},"x":{"0":226.9400024414,"1":354.7524719238,"2":234.8511962891,"3":307.1087646484,"4":"0","5":307.1087646484,"6":338.8617248535,"7":"0"},"y":{"0":-8.8123865128,"1":-72.7444534302,"2":-96.7423095703,"3":-74.8153915405,"4":"0","5":-74.8153915405,"6":-56.0145263672,"7":"0"},"z":{"0":142.8887023926,"1":72.2275466919,"2":61.2597045898,"3":-57.2363128662,"4":"0","5":-57.2363128662,"6":71.1682739258,"7":"0"}}'
@socketio.on("instrucao_teste")

def handle_message(data):
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento error_status"})
    socketio.emit('instrucao', {"instrucao":instrucao, "id_montagem": 3})
    print(f"Mensagem recebida: {data}")