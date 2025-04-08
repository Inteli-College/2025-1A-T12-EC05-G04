import os
import eventlet
eventlet.monkey_patch()  # Faz o monkey patch para suportar I/O não bloqueante

from app import app, socketio  # Certifique-se de que o objeto socketio está sendo importado

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Execute utilizando o socketio.run, que internamente usa eventlet
    socketio.run(app, debug=True, host='localhost', port=port)

    # app.run(debug=True,host='0.0.0.0', port=port)
