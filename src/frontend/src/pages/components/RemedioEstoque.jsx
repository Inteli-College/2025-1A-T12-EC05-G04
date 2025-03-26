import React from "react";

export default function RemedioEstoque() {
    return (
        <div className="remedio-estoque-container">
            <div className="remedio-estoque-nome">
                <p>Nome do remédio</p>
            </div>
            <div className="remedio-estoque-unidades">
                <p>x unidades</p>
            </div>
            <div className="remedio-estoque-pedido">
                <button className="remedio-estoque-pedido-button">Fazer pedido</button>
            </div>
        </div>
    )
}