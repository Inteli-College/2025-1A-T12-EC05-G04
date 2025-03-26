import socketio
import logging
from lerQR import lerQR

# from serial.tools import list_ports

# aval = list_ports.comports()

# print(f"{[x.device for x in aval]}")

# Crie uma instância do cliente Socket.IO
sio = socketio.Client()

@sio.event
def connect():
    print('Conectado ao servidor!')

@sio.event
def disconnect():
    print('Desconectado do servidor.')

@sio.event
def chat_message(data):
    print(f"Mensagem no canal 'chat_message': {data}")

logging.basicConfig(level=logging.DEBUG)

def send_message(data):
    """Envia mensagens WebSocket, comporta dois parâmetros, event e message."""
    sio.emit(data)

def listen_instrucao(data):
    print(f"Mensagem recebida: {data}")
    return data

# Conecte-se ao servidor Socket.IO
sio.connect('http://localhost:5000')  # Substitua pela URL do seu servidor

#
sio.on('instrucao')(listen_instrucao)

# Aguarde eventos indefinidamente
sio.wait()