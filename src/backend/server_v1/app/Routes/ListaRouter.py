from flask import Blueprint, jsonify, request
from app.Controllers.ListaController import ListaController

lista_router_bp = Blueprint("lista", __name__, url_prefix="/lista")
lista_controller = ListaController()  # instanciando o controller

@lista_router_bp.route("/create", methods=["GET", "POST"])
def router_create_listaAndMontagem():

        dados_nova_lista = request.get_json()
        res, status_code, nova_lista = lista_controller.createListaAndMontagem(dados_nova_lista)
        return jsonify(res), status_code, None

@lista_router_bp.route("/all", methods=["GET"])
def router_getAll_lista():
    res, status_code = lista_controller.getAllListas()
    return jsonify(res), status_code

@lista_router_bp.route("/<int:id_lista>", methods=["GET"])
def router_getById_lista(id_lista):
    res, status_code = lista_controller.getByIdLista(id_lista)
    return jsonify(res), status_code

