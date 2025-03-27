from flask_socketio import SocketIO, emit
from app.QueueManager import add_message

# Depois mudar a origem da conexão para o do Raspberry
socketio = SocketIO(cors_allowed_origins="*")  

@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("message")
def handle_message(data):
    socketio.emit("Data", "fodasse")
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
