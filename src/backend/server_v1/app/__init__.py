# Configuração para iniciar o servidor

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from app.configuration import ProductionConfig, DevelopmentConfig
from app.Websockets import socketio
import os
import eventlet
import eventlet.wsgi

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config.from_object(ProductionConfig)


socketio.init_app(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))
os.makedirs(os.path.join(basedir, 'migrations/versions'), exist_ok=True)

from app.Models import DevolucaoModel, ErroMontagemModel, ListaModel, LogsModel, LoteModel, MontagemModel, PacienteModel, UsuarioModel, InstrucaoRoboModel

from app.Routes.CodigosRota import codigo_bp
app.register_blueprint(codigo_bp)

from app.Routes.ListaRouter import lista_router_bp
app.register_blueprint(lista_router_bp)

from app.Routes.MontagemRouter import montagem_router_bp
app.register_blueprint(montagem_router_bp)

from app.Routes.LogsRouter import log_router_bp
app.register_blueprint(log_router_bp)

from app.Routes.UsuarioRouter import auth_router_bp
app.register_blueprint(auth_router_bp)

from app.Routes.InstrucaoRoboRouter import instrucaoRobo_router_bp
app.register_blueprint(instrucaoRobo_router_bp)
