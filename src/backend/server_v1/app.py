# Arquivo responsável por iniciar a aplicação

import os
from app import app, socketio

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Iniciando a aplicação SocketIO na porta {port}...")  # <-- print adicionado
    socketio.run(app, host='localhost', port=port)
