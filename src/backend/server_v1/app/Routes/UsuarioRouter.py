from flask import Blueprint, jsonify, request
from app.Controllers.UserController import UsuarioController

auth_router_bp = Blueprint("auth", __name__, url_prefix="/auth")
usuario_controller = UsuarioController()

@auth_router_bp.route("/login", methods=["POST"]) # mandar os dados para o servidor
def router_auth_user():
    dados_auth_user = request.get_json()
    res, status_code = usuario_controller.login(dados_auth_user)
    return jsonify(res), status_code


@auth_router_bp.route("/create", methods=["POST"])
def create_new_user():
        dados_new_user = request.get_json()
        res, status_code = usuario_controller.createUsuario(dados_new_user)
        return jsonify(res), status_code
