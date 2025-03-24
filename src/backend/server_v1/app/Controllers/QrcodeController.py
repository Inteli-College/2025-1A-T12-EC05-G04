from os import abort
from app.Models.Models import db

class QrcodeController:

    def __init__(self):
        pass
    
    def getByid_qrcode(self, id):
        try:
            id = int(id)
        except ValueError:
            # Levante uma exceção ou trate o erro conforme necessário
            abort(400, description="ID inválido")
        # qrcodeByid = CodigoBipado.query.get_or_404(id)
        # return qrcodeByid

    
    def getAll_qrcode(self):
        # qrcodeAll = CodigoBipado.query.all()
        # Refazer o controlleer conforme o novo banco de dados
        return "oi"