import React, { useState } from "react";
import styles from "../../styles/SearchBarEstoque.module.css";

export default function SearchBar({ onSearch, onSort }) {
    const [searchTerm, setSearchTerm] = useState("");
    const [filterBy, setFilterBy] = useState("remedio");
    const [sortBy, setSortBy] = useState("alfabetico");
    const [direction, setDirection] = useState("asc");

    const handleSearchChange = (e) => {
        setSearchTerm(e.target.value);
        onSearch(e.target.value, filterBy);
    };

    const handleFilterChange = (e) => {
        setFilterBy(e.target.value);
        onSearch(searchTerm, e.target.value);
    };

    const handleSortChange = (e) => {
        const value = e.target.value;
        setSortBy(value);
        onSort(value, direction);
    };

    const handleDirectionChange = (e) => {
        const value = e.target.value;
        setDirection(value);
        onSort(sortBy, value);
    };

    return (
        <div className={styles.container}>
            <input
                type="text"
                placeholder="Pesquise aqui"
                className={styles.input}
                value={searchTerm}
                onChange={handleSearchChange}
            />
            <select value={filterBy} onChange={handleFilterChange} className={styles.select}>
                <option value="remedio">Nome</option>
                <option value="codigo">Código</option>
            </select>
            <select value={sortBy} onChange={handleSortChange} className={styles.select}>
                <option value="alfabetico">Nome</option>
                <option value="codigo">Código</option>
                <option value="dose">Dose</option>
                <option value="validade">Validade</option>
                <option value="quantidade">Quantidade</option>
            </select>
            <select value={direction} onChange={handleDirectionChange} className={styles.select}>
                <option value="asc">Crescente</option>
                <option value="desc">Decrescente</option>
            </select>
        </div>
    );
}
