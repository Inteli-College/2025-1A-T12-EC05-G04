# Arquivo resposabilizado por iniciar a aplicação

import os
from app import app, socketio


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5556))
	socketio.run(app, host='127.0.0.1', port=port, debug=True)