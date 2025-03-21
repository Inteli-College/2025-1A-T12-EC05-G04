import socketio
import logging
from lerQR import lerQR

# Crie uma instância do cliente Socket.IO
sio = socketio.Client()

# Defina os eventos que você quer escutar
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

# Conecte-se ao servidor Socket.IO
sio.connect('http://localhost:5000')  # Substitua pela URL do seu servidor

qrLido = lerQR()

# Envie uma mensagem para o "canal" chat_message
sio.emit('message', {qrLido})

# Aguarde eventos indefinidamente
sio.wait()