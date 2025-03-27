from flask import Blueprint, jsonify, request
from app.Controllers.InstrucaoRoboController import InstrucaoRoboController

instrucaoRobo_router_bp = Blueprint("instrucaoRobo", __name__, url_prefix="/instrucaoRobo")
instrucaoRobo_controller = InstrucaoRoboController()

@instrucaoRobo_router_bp.route("/<int:instrucaoRobo_id>", methods=["GET"])
def router_getByid_log(instrucaoRobo_id):
    res, status_code = instrucaoRobo_controller.getByIdInstrucaoRobo(instrucaoRobo_id)
    return jsonify(res), status_code