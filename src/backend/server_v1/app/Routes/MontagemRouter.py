from flask import Blueprint, jsonify, request
from app.Controllers.MontagemController import MontagemController

montagem_router_bp = Blueprint("montagem", __name__, url_prefix="/montagem")
montagem_controller = MontagemController()

# Rotas Montagem
# A criação (POST) de Montagens é criada pelo ListaController e aplicada em ListaRouter
@montagem_router_bp.route("/<int:id_montagem>", methods=["GET"])
def router_getByid_montagem(id_montagem):
    res, status_code = montagem_controller.getByIdMontagem(id_montagem)
    return jsonify(res), status_code

@montagem_router_bp.route("/all", methods=["GET"])
def router_getAll_montagem():
    res, status_code = montagem_controller.getAllMontagem()
    return jsonify(res), status_code

@montagem_router_bp.route("/pendentes", methods=["GET"])
def router_getPendentes_montagem():
    res, status_code = montagem_controller.getPendentesMontagem()
    return jsonify(res), status_code

@montagem_router_bp.route("/delete/<int:id_montagem>", methods=["DELETE"])
def router_delete_montagem(id_montagem):
    res, status_code = montagem_controller.deleteMontagem(id_montagem)
    return jsonify(res), status_code

@montagem_router_bp.route("/update/<int:id_montagem>", methods=["PATCH"])
def router_update_montagem(id_montagem):
    dados_update_montagem = request.get_json()
    res, status_code = montagem_controller.updateMontagem(id_montagem, dados_update_montagem)
    return jsonify(res), status_code


# Rotas ErroMontagem
@montagem_router_bp.route("/error/all", methods=["GET"])
def router_getAll_ErroMontagem():
    res, status_code = montagem_controller.getAllErroMontagem()
    return jsonify(res), status_code

@montagem_router_bp.route("/error/create", methods=["POST"])
def router_create_ErroMontagem():
        dados_novo_erroMontagem = request.get_json()
        res, status_code = montagem_controller.createErroMontagem(dados_novo_erroMontagem)
        return jsonify(res), status_code