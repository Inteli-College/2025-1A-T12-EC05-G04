# Configuração para iniciar o servidor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.Websockets import socketio

app = Flask(__name__)
app.config.from_object('app.configuration.DevelopmentConfig')
socketio.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.Models import Models

from app.Routes.CodigosRota import codigo_bp
app.register_blueprint(codigo_bp)