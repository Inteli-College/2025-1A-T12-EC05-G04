import { useEffect, useState } from "react";
import axios from "axios";

import SideBar from "./components/Sidebar";
import MontagemItem from "./components/MontagemItem";
import styles from '../styles/Pendentes.module.css';

export default function Pendentes() {
  const [montagens, setMontagens] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/montagem/pendentes")
      .then((res) => {
        console.log("Montagens recebidas:", res.data); // <-- isso aqui
        setMontagens(res.data);
      })
      .catch((err) => {
        console.error("Erro ao buscar montagens:", err);
      });
  }, []);

  return (
    <div className="screen">
      <SideBar />
      <div className="content">
        <h1 className="montagem-title">Montagens Pendentes</h1>
        {montagens.length === 0 ? (
          <p>Nenhuma montagem pendente encontrada.</p>
        ) : (
          montagens.map((m) => (
            <MontagemItem
              key={m.id}
              id={m.id}
              nomePaciente={m.nome_paciente}
              hc={m.hc}
              leito={m.leito}
              datetime={m.datetime}
            />
          ))
        )}
      </div>
    </div>
  );
}
