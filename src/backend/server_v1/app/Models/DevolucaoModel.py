from app import db

class Devolucao(db.Model):
    __tablename__ = 'devolucao'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.String(20), nullable=False)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    quantidade = db.Column(db.String(10), nullable=False)

    
    def __repr__(self):
        return f'<Devolucao {self.id}>'