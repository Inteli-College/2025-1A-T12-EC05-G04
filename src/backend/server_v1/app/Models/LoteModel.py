from app import db

class Lote(db.Model):
    __tablename__ = 'lote'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    remedio = db.Column(db.String(100), nullable=False)
    compostoAtivo = db.Column(db.String(10), nullable=False)  
    dose = db.Column(db.String(10), nullable=False)
    validade = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.String(10), nullable=False)
    codigo = db.Column(db.String(100), nullable=False)
    
    # Relacionamentos
    listas = db.relationship('Lista', backref='lote', lazy=True)
    devolucoes = db.relationship('Devolucao', backref='lote', lazy=True)
    
    # Ajuste do relacionamento com Logs: se quiser referenciar o Lote em Logs,
    # a foreign key de Logs deve ser 'lote.id', e aqui o backref deve ser 'lote'
    logs = db.relationship('Logs', backref='lote', lazy=True)

    def __repr__(self):
        return f'<Lote {self.remedio}>'