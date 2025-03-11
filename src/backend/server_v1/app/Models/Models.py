# Arquivo resposável por modelar/manipular o banco de dados
# Obs: Apenas de exemplo

from app import db

class CodigoBipado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_barra = db.Column(db.String(250))
        
    def to_dict(self):
        return {
            "id": self.id,
            "codigo_barra": self.codigo_barra
        }
