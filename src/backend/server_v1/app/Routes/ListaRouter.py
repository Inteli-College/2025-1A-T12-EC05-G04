from flask import Blueprint, jsonify, request
from app.Controllers.ListaController import ListaController

lista_router_bp = Blueprint("lista", __name__, url_prefix="/lista")
lista_controller = ListaController()  # instanciando o controller

@lista_router_bp.route("/create", methods=["POST"])
def router_create_listaAndMontagem():
    dados_nova_lista = request.get_json()
    res, status_code, nova_lista = lista_controller.createListaAndMontagem(dados_nova_lista)
    return jsonify(res), status_code, None


@lista_router_bp.route("/emergencia", methods=["GET"])
def router_getRemediosDisponiveis():
    res, status_code = lista_controller.getRemediosDisponiveis()
    return jsonify(res), status_code

@lista_router_bp.route("/emergencia/forms", methods=["POST"])
def router_createFromFormulario():
    dados_emergencia_lista = request.get_json()
    res, status_code = lista_controller.createFromFormulario(dados_emergencia_lista)
    return jsonify(res), status_code