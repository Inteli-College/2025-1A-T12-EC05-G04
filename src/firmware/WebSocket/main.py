import socketio
import logging

# from serial.tools import list_ports

# aval = list_ports.comports()

# print(f"{[x.device for x in aval]}")

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

def send_message(event, data):
    """Envia mensagens WebSocket, comporta dois parâmetros, event e message."""
    sio.emit(event, data)

    # Tem que mandar para o qr_code, status e receber da instrucao message_status

@sio.on("instrucao")
def listen_instrucao(data):
    print(f"Mensagem recebida: {data}")    


if __name__ == "__main__":
    sio.connect('http://localhost:5000')  # Substitua pela URL do seu servidor
    send_message('instrucao', "O raspberry está conectado!")
    print("Mensagem enviada!")
    sio.wait()

