import React, { useState, useEffect } from 'react';
import SideBar from './components/Sidebar';
import RemedioEstoque from './components/RemedioEstoque';
import SearchBar from './components/SearchBar';
import styles from '../styles/Estoque.module.css'

export default function Estoque() {
    return (
        <div className="screen">
            <SideBar />
            <div className="content">
                <div className={styles.containerGeral}>
                    <h1 className={styles.title}>Estoque</h1>
                    <SearchBar />
                    <RemedioEstoque />
                </div>
            </div>
        </div>
    );
}