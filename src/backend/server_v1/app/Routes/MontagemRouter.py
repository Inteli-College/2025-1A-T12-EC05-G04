from flask import Blueprint, jsonify, request
from app.Controllers.MontagemController import MontagemController

montagem_router_bp = Blueprint("montagem", __name__, url_prefix="/montagem")
montagem_controller = MontagemController()

# Endpoint de GET Montagem por id
@montagem_router_bp.route("/<int:id_montagem>", methods=["GET"])
def router_getByid_montagem(id_montagem):
    res, status_code = montagem_controller.getByIdMontagem(id_montagem)
    return jsonify(res), status_code

# Endpoint de GET todas as Montagem 
@montagem_router_bp.route("/all", methods=["GET"])
def router_getAll_montagem():
    res, status_code = montagem_controller.getAllMontagem()
    return jsonify(res), status_code

# Endpoint de GET todas as Montagem 
@montagem_router_bp.route("/pendentes", methods=["GET"])
def router_getPendentes_montagem():
    res, status_code = montagem_controller.getPendentesMontagem()
    return jsonify(res), status_code

# Endpoint de DELETE Montagem por id 
@montagem_router_bp.route("/delete/<int:id_montagem>", methods=["DELETE"])
def router_delete_montagem(id_montagem):
    res, status_code = montagem_controller.deleteMontagem(id_montagem)
    return jsonify(res), status_code


# # Endpoint de UPDATE Montagem por id 
# @montagem_router.route("/update/<int:id_montagem>", methods=["UPDATE"])
# def router_update_montagem(id_montagem):
#     res = MontagemController.updateMontagem(id_montagem)
#     return jsonify(res), 200


# my name is gabriel == my name is gay bro
# by Gabs