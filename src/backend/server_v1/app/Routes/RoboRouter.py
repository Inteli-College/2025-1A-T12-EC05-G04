from flask import Blueprint, jsonify, request
from app.Controllers.RoboController import RoboController
from app.Controllers.ListaController import ListaController

robo = RoboController
lista = ListaController

robo_bp = Blueprint("robo", __name__, url_prefix="/robo")

@robo_bp.route("/", methods=["POST"])
def iniciar_montagem():    
    data = request.json
    return robo.iniciarMontagem(data)


@robo_bp.route("/stop", methods=["GET"])
def parar_montagem():
    print("")

@robo_bp.route("/", methods=["DELETE"])
def deletar_montagem():
    print("")