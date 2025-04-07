from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from app.configuration import ProductionConfig, DevelopmentConfig

import os

app = Flask(__name__)

# Configurações de ambiente
app.config.from_object(DevelopmentConfig)
app.config.from_object(ProductionConfig)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

basedir = os.path.abspath(os.path.dirname(__file__))
os.makedirs(os.path.join(basedir, 'migrations/versions'), exist_ok=True)

# Importa models
from app.Models import (
    DevolucaoModel,
    ErroMontagemModel,
    ListaModel,
    LogsModel,
    LoteModel,
    MontagemModel,
    PacienteModel,
    UsuarioModel,
    InstrucaoRoboModel
)

# Registra as rotas
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

from app.Routes.RoboRouter import robo_bp
app.register_blueprint(robo_bp)

from app.Routes.LoteRouter import lote_router_bp
app.register_blueprint(lote_router_bp)

from app.Routes.PacientesRouter import pacientes_bp
app.register_blueprint(pacientes_bp)

from app.Websockets import socketio
socketio.init_app(app)
