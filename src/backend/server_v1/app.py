# Arquivo responsável por iniciar a aplicação

import os
from app import app, socketio

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # socketio.run(app, host='localhost', port=port)
    app.run(debug=True,host='0.0.0.0', port=port)
