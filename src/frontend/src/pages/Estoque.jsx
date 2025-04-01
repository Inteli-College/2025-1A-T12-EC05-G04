import React, { useState, useEffect } from 'react';
import SideBar from './components/Sidebar';
import RemedioEstoque from './components/RemedioEstoque';
import SearchBar from './components/SearchBar';
import styles from '../styles/Estoque.module.css'
import RemedioVencimento from './components/RemedioVencimento';

export default function Estoque() {
    return (
        <div className="screen">
            <SideBar />
            <div className="content">
                <h1 className={styles.title}>Estoque</h1>
                <SearchBar />
                <div className={styles.containerGeral}>
                <h2>Medicamentos próximos de acabar</h2>
                    <RemedioEstoque />
                    <RemedioEstoque />
                    <RemedioEstoque />
                <h2>Medicamentos próximos do vencimento</h2>
                    <RemedioVencimento />
                    <RemedioVencimento />
                    <RemedioVencimento />
                </div>
            </div>
        </div>
    );
}