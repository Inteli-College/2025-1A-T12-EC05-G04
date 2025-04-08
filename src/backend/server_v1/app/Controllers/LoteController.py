from app.Models.LoteModel import Lote  # ou só Lote se já for importado assim
from app import db

class LoteController:
    def getLotes(self):
        try:
            lotes = Lote.query.all()
            resultado = []

            for lote in lotes:
                resultado.append({
                    "id": lote.id,
                    "remedio": lote.remedio,
                    "compostoAtivo": lote.compostoAtivo,
                    "dose": lote.dose,
                    "validade": lote.validade,
                    "quantidade": lote.quantidade,
                    "codigo": lote.codigo
                })

            return {"lotes": resultado}, 200

        except Exception as e:
            return {"erro": str(e)}, 500
