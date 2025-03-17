from flask import Blueprint
from app.Controllers.CodigosController import CodigosController

codigo_bp = Blueprint("codigo", __name__, url_prefix="/codigo")


@codigo_bp.route("/")
def post_codigo():
    
    codigo_controller = CodigosController()
    msg = codigo_controller.post_codigo()
    return msg

    