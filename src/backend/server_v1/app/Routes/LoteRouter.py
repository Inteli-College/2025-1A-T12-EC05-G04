from flask import Blueprint, jsonify
from app.Controllers.LoteController import LoteController

lote_router_bp = Blueprint("lotes", __name__, url_prefix="/lotes")
lote_controller = LoteController()

@lote_router_bp.route("/", methods=["GET"])
def get_lotes():
    res, status_code = lote_controller.getLotes()
    return jsonify(res), status_code
