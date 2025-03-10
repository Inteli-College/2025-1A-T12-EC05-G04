from app.QueueManager import get_message
from app.Models.Models import CodigoBipado, db

class CodigosController:

    def __init__(self):
        pass
    
    def post_codigo(self):
        codigo = get_message()
        
        new = CodigoBipado(codigo_barra=codigo)
        db.session.add(new)
        db.session.commit()
        print(f"Adicionado ao banco com sucesso!")

        return codigo