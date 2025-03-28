from flask_socketio import SocketIO
from app.QueueManager import add_message
import logging

# Depois mudar a origem da conexão para o do Raspberry
socketio = SocketIO(cors_allowed_origins="*")  

@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("message")
def handle_message(data):
    socketio.emit("Mensagem recebida no servidor! :D")
    print(f"Mensagem recebida: {data}")
    add_message(data)  

@socketio.on("qr_code")
def handle_message(data):    
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server!"})
    print(f"Mensagem recebida: {data}")
    add_message(data)  

@socketio.on("instrucao_fe")
def handle_message(data): 
    socketio.emit('message_status', {"message":"Mensagem recebida pelo server!"})   
    socketio.emit('instrucao',{"instrucao":data})
    print(f"Mensagem recebida: {data}")

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
