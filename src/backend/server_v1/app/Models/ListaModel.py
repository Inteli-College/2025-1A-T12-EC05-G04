from app import db

class Lista(db.Model):
    __tablename__ = 'lista'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    
    # Seria mais lógico armazenar a quantidade como Integer, mas se preferir String, pode manter
    quantidade = db.Column(db.String(10), nullable=False)
    
    # Relacionamento 1:1 com Montagem
    montagem = db.relationship('Montagem', uselist=False, back_populates='lista')
    
    def __repr__(self):
        return f'<Lista {self.id}>'