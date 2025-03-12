# Configuração para iniciar o servidor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.configuration import ProductionConfig, DevelopmentConfig
from app.Websockets import socketio

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_object(ProductionConfig)


socketio.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.Models import Models

from app.Routes.CodigosRota import codigo_bp
app.register_blueprint(codigo_bp)

from app.Routes.QrcodeRouter import qrcode_bp
app.register_blueprint(qrcode_bp)