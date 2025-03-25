from app import db

class Logs(db.Model):
    __tablename__ = 'logs'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_montagem = db.Column(db.Integer, db.ForeignKey('montagem.id'), nullable=False)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    
    datetime = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<Logs {self.id}>'