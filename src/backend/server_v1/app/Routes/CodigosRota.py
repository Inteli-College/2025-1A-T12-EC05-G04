from flask import Blueprint
from app.Controllers.CodigosController import CodigosController

codigo_bp = Blueprint("codigo", __name__, url_prefix="/codigo")


@codigo_bp.route("/")
def get_codigo():
    
    codigo_controller = CodigosController()

    msg = codigo_controller.get_codigo()

    if msg:
        return f"A rota recebeu: {msg}"
    
    return "Nenhuma mensagem recebida..."

    