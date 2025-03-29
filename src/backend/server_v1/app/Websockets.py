from flask_socketio import SocketIO
from app.QueueManager import add_message
import logging
import json

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

@socketio.on("log")
def handle_log(data):
    try:
        data = parse_socketio_payload(data)
        if isinstance(data, str):
            data = json.loads(data)
        print("[WS] Evento 'log' recebido:", data)

        if not isinstance(data, dict):
            print(" Ignorado: payload não é dicionário")
            return
        if "medicineName" not in data or "progress" not in data:
            print(" Ignorado: campos obrigatórios ausentes")
            return

        socketio.emit("log", data)
    except Exception as e:
        print("❌ Erro ao processar 'log':", str(e))

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
        print("❌ Erro ao parsear payload socket.io:", e)
        return None