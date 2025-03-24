from flask import Blueprint, jsonify, request
from app.Controllers.PacientesController import PacientesController

pac = PacientesController()

pacientes_bp = Blueprint("pacientes", __name__, url_prefix="/pacientes")

@pacientes_bp.route("/", methods=["POST"])
def post_paciente():
    data = request.json
    return pac.post_paciente(data)

@pacientes_bp.route("/", methods=["GET"])
def get_pacientes():
    return pac.get_pacientes()

@pacientes_bp.route("/id", methods=["GET"])
def get_id_paciente():
    data = request.json
    return pac.get_id_paciente(data)

@pacientes_bp.route("/nome", methods=["GET"])
def get_nome_paciente():
    data = request.json
    return pac.get_nome_paciente(data)

@pacientes_bp.route("/", methods=["PUT"])
def put_paciente():
    data = request.json
    return pac.put_paciente(data)

@pacientes_bp.route("/", methods=["DELETE"])
def delete_paciente():
    data = request.json
    return pac.delete_paciente(data)