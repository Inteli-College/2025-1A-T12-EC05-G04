from flask_socketio import SocketIO, emit
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
    socketio.emit("Mensagem recebida no servidor! :D")
    print(f"Mensagem recebida: {data}")
    add_message(data)  

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")


import time

@socketio.on('add_medicine')
def handle_add_medicine(data):
    name = data['name']
    print(f"[WS] Evento add_medicine recebido: {name}")

    for progress in [0, 25, 50, 75, 100]:
        socketio.emit('log', {
            'medicineName': data['name'],
            'progress': 0,
            'message': 'Início da montagem'
        })

        time.sleep(1)  # delay para simular tempo real
def send_message(event, data):
    """Envia mensagem Websocket"""
    try:
        socketio.emit(event,data)
        return {"status": "sucess", "message": "Mensagem enviada com sucesso! :D"}
    except Exception as e:
        logging.error(f"Erro ao enviar mensagem WebSocket: {e}")
        return {"status": "error", "message": f"Erro ao enviar mensagem: {str(e)}"}
