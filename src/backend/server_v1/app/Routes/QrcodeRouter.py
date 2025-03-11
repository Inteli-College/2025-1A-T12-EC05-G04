from flask import Blueprint, jsonify
from app.Controllers.QrcodeController import QrcodeController

qrcode_bp = Blueprint("qrcode", __name__, url_prefix="/qrcode")

@qrcode_bp.route("/id=<id>", methods=["GET"])
def getByid_qrcode(id):
    
    qrcode_controller = QrcodeController()
    res =  qrcode_controller.getByid_qrcode(id)  

    return jsonify(res.to_dict()), 200

@qrcode_bp.route("/all", methods=["GET"])
def getAll_qrcode():
    
    qrcode_controller = QrcodeController()
    lista = qrcode_controller.getAll_qrcode()
    list_dict = [obj.to_dict() for obj in lista]

    return jsonify(list_dict), 200

