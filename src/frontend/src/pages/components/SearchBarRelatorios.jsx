import React, { useState } from "react";
import styles from "../../styles/SearchBarEstoque.module.css";

export default function SearchBarRelatorios({ onSearch }) {
    const [turno, setTurno] = useState("");
    const [dataInicio, setDataInicio] = useState("");
    const [dataFim, setDataFim] = useState("");
    const [ala, setAla] = useState("");

    const handleSearch = () => {
        onSearch({
            turno,
            dataInicio,
            dataFim,
            ala
        });
    };

    const handleClearFilters = () => {
        setTurno("");
        setDataInicio("");
        setDataFim("");
        setAla("");
        onSearch({
            turno: "",
            dataInicio: "",
            dataFim: "",
            ala: ""
        });
    };

    return (
        <div className={styles.container}>
            {/* Turno */}
            <select
                value={turno}
                onChange={(e) => {
                    setTurno(e.target.value);
                    handleSearch();
                }}
                className={styles.select}
            >
                <option value="">Todos os turnos</option>
                <option value="manha">Manhã</option>
                <option value="tarde">Tarde</option>
                <option value="noite">Noite</option>
                <option value="madrugada">Madrugada</option>
            </select>

            {/* Período */}
            <input
                type="date"
                value={dataInicio}
                onChange={(e) => {
                    setDataInicio(e.target.value);
                    handleSearch();
                }}
                className={styles.select}
            />
            <input
                type="date"
                value={dataFim}
                onChange={(e) => {
                    setDataFim(e.target.value);
                    handleSearch();
                }}
                className={styles.select}
            />

            {/* Ala médica */}
            <select
                value={ala}
                onChange={(e) => {
                    setAla(e.target.value);
                    handleSearch();
                }}
                className={styles.select}
            >
                <option value="">Todas as alas</option>
                <option value="pediatria">Pediatria</option>
                <option value="uti">UTI</option>
                <option value="cardiologia">Cardiologia</option>
            </select>

            {/* Botão limpar filtros */}
            <button onClick={handleClearFilters} className={styles.clearButton}>
                Limpar filtros
            </button>
        </div>
    );
}
