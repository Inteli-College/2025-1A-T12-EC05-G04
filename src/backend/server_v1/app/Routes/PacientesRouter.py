from flask import Blueprint, jsonify, request
from app.Controllers.PacientesController import PacientesController
from flask_cors import cross_origin


pac = PacientesController()

pacientes_bp = Blueprint("pacientes", __name__, url_prefix="/pacientes")

@pacientes_bp.route("/", methods=["POST"])
def post_paciente():
    data = request.json
    return pac.postPaciente(data)

@pacientes_bp.route("/", methods=["GET"])
def get_pacientes():
    return pac.getPacientes()

@pacientes_bp.route("/id", methods=["GET"])
def get_id_paciente():
    data = request.json
    return pac.getIdPaciente(data)

@pacientes_bp.route("/nome", methods=["GET"])
def get_nome_paciente():
    data = request.json

    if isinstance(data['nome'], str):
        return pac.getNomePaciente(data)
    
    if isinstance(data['leito'], str):
        return pac.getLeitoPaciente(data)

@pacientes_bp.route("/", methods=["PUT"])
def put_paciente():
    data = request.json
    return pac.putPaciente(data)

@pacientes_bp.route("/", methods=["DELETE"])
def delete_paciente():
    data = request.json
    return pac.deletePaciente(data)

@pacientes_bp.route("/validar/<string:hc_paciente>", methods=["GET"])
@cross_origin(supports_credentials=True)
def validar_paciente(hc_paciente):
    # Sua lógica para buscar o paciente pelo HC
    paciente, status = pac.getHCPaciente(hc_paciente)
    if status == 200:
        # Retorna os dados do paciente em JSON
        return jsonify({"nome": paciente.nome, "leito": paciente.Leito}), 200
    else:
        return jsonify(paciente), 404
