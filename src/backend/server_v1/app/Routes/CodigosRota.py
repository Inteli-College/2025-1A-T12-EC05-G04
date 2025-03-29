from flask import Blueprint
from app.Controllers.CodigosController import QrCodeController

codigo_bp = Blueprint("codigo", __name__, url_prefix="/codigo")


@codigo_bp.route("/")
def router_post_codigo():
    
    codigo_controller = QrCodeController()

    msg = codigo_controller.post_codigo()

    if msg:
        return f"A rota recebeu: {msg}"
    
    return "Nenhuma mensagem recebida..."