import React, { useEffect, useState } from "react";
import axios from "axios"; // faz requisição HTTP ao backend
import MontagemItem from "./MontagemItem"; 

export default function MontagensPendentes() {
    const [montagens, setMontagens] = useState([]);
  
    useEffect(() => { // executado automaticamente quando o componente é montado na tela
      axios.get("http://localhost:5000/montagem/pendentes") // faz uma requisição GET
        .then((res) => {
          console.log("Montagens recebidas:", res.data); // só pra debug
          setMontagens(res.data);
        })
        .catch((err) => {
          console.error("Erro ao buscar montagens:", err);
        });
    }, []);
  
    return (
      <div>
        <h1>Montagens Pendentes</h1>
  
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
    );
  }