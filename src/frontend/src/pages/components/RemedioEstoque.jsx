import React from "react";
import styles from "../../styles/RemedioEstoque.module.css";

export default function RemedioEstoque({ lote }) {
    return (
        <div className={styles.card}>
            <div className={styles.topo}>
                <p className={styles.nome}><strong>{lote.remedio}</strong></p>
                <p className={styles.codigo}>Código: {lote.codigo}</p>
            </div>
            <div className={styles.detalhes}>
                <p>Dose: {lote.dose}</p>
                <p>Validade: {new Date(lote.validade).toLocaleDateString('pt-BR')}</p>
                <p>Quantidade: {lote.quantidade} unidades</p>
            </div>
        </div>
    );
}
