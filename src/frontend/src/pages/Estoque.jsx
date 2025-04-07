import React, { useState, useEffect } from 'react';
import SideBar from './components/Sidebar';
import RemedioEstoque from './components/RemedioEstoque';
import SearchBar from './components/SearchBarEstoque';
import styles from '../styles/Estoque.module.css';

export default function Estoque() {
    const [lotes, setLotes] = useState([]);
    const [filtro, setFiltro] = useState("remedio");
    const [busca, setBusca] = useState("");
    const [ordenacao, setOrdenacao] = useState("alfabetico");
    const [direcao, setDirecao] = useState("asc");

    useEffect(() => {
        fetch("http://localhost:5000/lotes/")
            .then(res => res.json())
            .then(data => setLotes(data.lotes))
            .catch(err => console.error("Erro ao buscar lotes:", err));
    }, []);

    const filtrarELotes = () => {
        let filtrados = [...lotes];

        if (busca) {
            filtrados = filtrados.filter(lote =>
                lote[filtro] && lote[filtro].toLowerCase().includes(busca.toLowerCase())
            );
        }

        const aplicarOrdem = (a, b, valor) => {
            if (typeof a[valor] === "string") {
                return a[valor].localeCompare(b[valor]);
            } else if (valor === "validade") {
                return new Date(a[valor]) - new Date(b[valor]);
            } else {
                return a[valor] - b[valor];
            }
        };

        let valorOrdenacao = ordenacao === "alfabetico" ? "remedio" : ordenacao;

        filtrados.sort((a, b) => {
            const resultado = aplicarOrdem(a, b, valorOrdenacao);
            return direcao === "asc" ? resultado : -resultado;
        });

        return filtrados;
    };

    return (
        <div className="screen">
            <SideBar />
            <div className="content">
                <h1 className={styles.title}>Estoque</h1>
                <SearchBar
                    onSearch={(valor, filtroSelecionado) => {
                        setBusca(valor);
                        setFiltro(filtroSelecionado);
                    }}
                    onSort={(tipo, direcaoSelecionada) => {
                        setOrdenacao(tipo);
                        setDirecao(direcaoSelecionada);
                    }}
                />
                <div className={styles.containerGeral}>
                    {filtrarELotes().map((lote) => (
                        <RemedioEstoque key={lote.id} lote={lote} />
                    ))}
                </div>
            </div>
        </div>
    );
}
