from flask_socketio import SocketIO
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
