from app.QueueManager import get_message

class CodigosController:

    def __init__(self):
        pass
    
    def post_codigo(self):
        codigo = get_message()

        return codigo