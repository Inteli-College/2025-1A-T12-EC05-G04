from flask_socketio import SocketIO
from app.QueueManager import QueueErrorStatus, QueueQrCode, QueueRoboStatus
import logging
import json
from app.Controllers.WsIntegracaoController import WsIntegracaoController

# Depois mudar a origem da conexão para o do Raspberry
socketio = SocketIO(cors_allowed_origins="*")  

queue_es = QueueErrorStatus
queue_qr = QueueQrCode
queue_rs = QueueRoboStatus

ws_controller = WsIntegracaoController

@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("robo_status")
def handle_message(data):
    """Recebe os Status do Robo e reenvia ao Front-End, antes fazendo consultas no banco para relacionar objetos com Id-Montagem.
    ---
    Conteúdos: acao, percentage e id_montagem
    ---
       Evento Recepção: robo_status
       Evento Emissão: robo_status_fe
    """

    socketio.emit('message_status', {"message":"Mensagem recebida no servidor no evento robo_status! :D"})
    print(f"Mensagem recebida: {data}")
    queue_rs.add_message(data)
    
    fe_friend = ws_controller.roboStatus()
    socketio.emit('robo_status_fe', fe_friend)  


@socketio.on("qr_code")
def handle_message(data):  
    """Recebe informações do Robo, caso as instruções sejam finalizadas com sucesso.
    ---
       Conteúdos: result, qr e id_montagem
       Relaciona esses conteúdos as tabelas(colunas):
       Montagem(status), Lote(codigo) e Montagem(datetime)
    ---
       Evento Recepção: qr_code
       Evento Emissão: None
    """

    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento qr_code! :D"})
    print(f"Mensagem recebida: {data}")
    queue_qr.add_message(data) 

    bd_friend = ws_controller.qrCode()
    print(bd_friend)


@socketio.on("error_status")
def handle_message(data):  
    """Recebe uma mensagem caso algo dê erro nos processos do robô.
    ---
       Conteúdos: message
    ---
       Evento Recepção: error_status       
    """

    socketio.emit('message_status', {"message":"Mensagem recebida pelo server no evento error_status"})
    print(f"Mensagem recebida: {data}")
    queue_es.add_message(data)  
    bd_friend = ws_controller.errorStatus()
    print(bd_friend) 
    
    socketio.emit('error_status_fe', bd_friend)


import json

@socketio.on("message_status_fe")
def handle_message_status_fe(data):
    try:
        data = parse_socketio_payload(data)

    except Exception as e:
        print(" Erro ao processar 'message_status_fe':", str(e))

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")

def send_message(event, data):
    """Função resposável por enviar mensagens WebSocket"""
    try:
        socketio.emit(event,data)
        return {"status": "sucess", "message": "Mensagem enviada com sucesso! :D"}
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem WebSocket: {e}")
        return {"status": "error", "message": f"Erro ao enviar mensagem: {str(e)}"}
    
def parse_socketio_payload(raw):
    """Extrai e decodifica o JSON do frame socket.io."""
    try:
        if isinstance(raw, str) and raw.startswith("42"):
            payload = raw[2:]  # remove o "42"
            return json.loads(payload)[1]  # [event, data]
        elif isinstance(raw, dict):
            return raw
        return None
    except Exception as e:
        print(" Erro ao parsear payload socket.io:", e)
        return None
