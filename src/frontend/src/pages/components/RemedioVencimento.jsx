import React from "react";

export default function RemedioVencimento() {
    return (
        <div className="remedio-estoque-container">
            <div className="remedio-estoque-nome">
                <p>Nome do remédio</p>
            </div>
            <div className="remedio-vencimento-data">
                <p>dd/mm/aa</p>
            </div>
            <div className="remedio-vencimento-lote">
                <p>Lote ID</p>
            </div>
            <div className="remedio-vencimento-quantidade">
                <p>Quantidade</p>
            </div>
        </div>
    )
}