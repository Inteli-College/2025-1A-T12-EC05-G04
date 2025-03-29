from app.QueueManager import QueueErrorStatus, QueueQrCode, QueueRoboStatus

class QrCodeController:

    def __init__(self):
        pass
    
    def post_codigo(self, data):
        message = data['message']
        qr_code = data['qr']
        id_montagem = data['id_montagem']

        return "shalallalalalal"