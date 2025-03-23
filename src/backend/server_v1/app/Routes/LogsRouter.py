from flask import Blueprint, jsonify, request
from app.Controllers.LogsController import LogsController

log_router_bp = Blueprint("log", __name__, url_prefix="/log")
logs_controller = LogsController()

@log_router_bp.route("/<int:log_id>", methods=["GET"])
def router_getByid_log(log_id):
    res, status_code = logs_controller.getByIdLog(log_id)
    return jsonify(res), status_code

@log_router_bp.route("/all", methods=["GET"])
def router_getAll_logs():
    res, status_code = logs_controller.getAllLogs()
    return jsonify(res), status_code

@log_router_bp.route("/create", methods=["POST"])
def router_post_log():
    dados_post_log = request.get_json()
    res, status_code = logs_controller.createLog(dados_post_log)
    return jsonify(res), status_code

