from app import db

class InstrucaoRobo(db.Model):
    __tablename__ = 'instrucaoRobo'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    
    instrucao = db.Column(db.String(255), nullable=False)
    
    # Relacionamentos
    lote = db.relationship('Lote', back_populates='instrucaoRobo')

    def __repr__(self):
        return f'<InstrucaoRobo {self.id}>'