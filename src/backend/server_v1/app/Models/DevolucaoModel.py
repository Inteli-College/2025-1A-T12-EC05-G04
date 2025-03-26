from app import db

class Devolucao(db.Model):
    __tablename__ = 'devolucao'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    datetime = db.Column(db.String(20), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return f'<Devolucao {self.id}>'