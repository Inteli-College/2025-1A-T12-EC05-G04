import React, { useState, useEffect } from "react";
import SideBar from "./components/Sidebar";
import axios from "axios";

// Função para retornar a data no formato YYYY-MM-DD
const getTodayDate = () => {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

export default function Emergencia() {
  const [emergencia, setEmergencia] = useState({
    nomePaciente: '',
    leito: '',
    hc: '',
    enfermeiro: '',
    date: getTodayDate(),
  });

  const usuarioLogado = JSON.parse(localStorage.getItem("usuario"));
  const [remediosDisponiveis, setRemediosDisponiveis] = useState([]);
  const [remediosSelecionados, setRemediosSelecionados] = useState([]);

  useEffect(() => {
    const fetchRemedios = async () => {
      try {
        const response = await axios.get("http://localhost:5000/lista/emergencia");
        setRemediosDisponiveis(response.data);
      } catch (error) {
        console.error("Erro ao buscar remédios:", error);
      }
    };
  
    fetchRemedios();

    // Atualiza o nome do enfermeiro com base no usuário logado
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    if (usuario && usuario.nome) {
      setEmergencia((prev) => ({
        ...prev,
        enfermeiro: usuario.nome
      }));
    }
  }, []);

  const handleSelecionarRemedio = (id, quantidadeMaxima) => {
    const jaSelecionado = remediosSelecionados.find((r) => r.id_remedio === id);
    if (jaSelecionado) {
      setRemediosSelecionados(remediosSelecionados.filter((r) => r.id_remedio !== id));
    } else {
      setRemediosSelecionados([...remediosSelecionados, { id_remedio: id, quantidade: 1, quantidadeMaxima }]);
    }
  };
  
  const handleQuantidadeChange = (id, novaQuantidade) => {
    setRemediosSelecionados((prev) =>
      prev.map((r) =>
        r.id_remedio === id ? { ...r, quantidade: parseInt(novaQuantidade) || 1 } : r
      )
    );
  };

  const handleChange = (e) => {
    setEmergencia({ ...emergencia, [e.target.name]: e.target.value });
  };  

  useEffect(() => {
    // MOCKANDO USUÁRIO LOGADO
    const usuarioMock = {
      id: 4,
      nome: "Roberto",
      email: "roberto@teste.com",
      cpf: "1222233444"
    };
    localStorage.setItem("usuario", JSON.stringify(usuarioMock));
  }, []);
  

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const dadosFormulario = {
      ...emergencia,
      enfermeiro_id: usuarioLogado?.id, // importante para associar a montagem
      remedios: remediosSelecionados.map((r) => ({
        id_remedio: r.id_remedio,
        quantidade: r.quantidade,
      })),
    };
  
    try {
      const response = await axios.post(
        "http://localhost:5000/lista/emergencia/forms",
        dadosFormulario,
        { mode: 'cors', headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ /* seus dados do formulário aqui */ }) }
      );
      console.log("Formulário enviado com sucesso:", response.data);
      // Aqui você pode exibir uma mensagem de sucesso ou redirecionar
    } catch (error) {
      console.error("Erro ao enviar dados:", error.response?.data || error.message);
      // Aqui você pode exibir uma mensagem de erro
    }
  };

  return (
    <div className="screen">
      <SideBar />
      <div className="content">
        <form onSubmit={handleSubmit}>
          <h1>Novo pedido de emergência</h1>
          <div className="emergencia-content">
            <div>
              <input 
                type="text" 
                id="nome-paciente"
                name="nomePaciente"
                placeholder="Nome do paciente"
                value={emergencia.nomePaciente}
                onChange={handleChange}
              />
              <div className="leito-hc">
                <input 
                  type="text"
                  id="leito" 
                  name="leito"
                  placeholder="Leito"
                  value={emergencia.leito}
                  onChange={handleChange}
                />
                <input 
                  type="text"
                  id="hc"
                  name="hc"
                  placeholder="HC"
                  value={emergencia.hc}
                  onChange={handleChange}
                />
              </div>
              <input 
                type="text"
                id="enfermeiro-responsavel"
                name="enfermeiro"
                placeholder="Enfermeiro responsável"
                value={emergencia.enfermeiro}
                readOnly
              />
              <div className="remedios-lista">
                <p><strong>Selecione os remédios:</strong></p>
                {remediosDisponiveis.map((remedio) => {
                  const selecionado = remediosSelecionados.find((r) => r.id_remedio === remedio.id);
                  return (
                    <div key={remedio.id} style={{ display: "flex", alignItems: "center", marginBottom: "8px" }}>
                      <label style={{ flex: 1 }}>
                        <input
                          type="checkbox"
                          checked={!!selecionado}
                          onChange={() => handleSelecionarRemedio(remedio.id, remedio.quantidade)}
                        />
                        {` ${remedio.remedio} (${remedio.dose}) - ${remedio.quantidade} disponíveis`}
                      </label>
                      {selecionado && (
                        <input
                          type="number"
                          min="1"
                          max={selecionado.quantidadeMaxima}
                          value={selecionado.quantidade}
                          onChange={(e) => handleQuantidadeChange(remedio.id, e.target.value)}
                          style={{
                            width: "60px",
                            marginLeft: "10px",
                            padding: "5px",
                            borderRadius: "4px",
                            border: "1px solid #ccc",
                            backgroundColor: "#fff",
                            color: "#000"
                          }}
                        />
                      )}
                    </div>
                  );
                })}
              </div>

            </div>
            <div id="emergencia-right">
              <input 
                type="date"
                id="date"
                name="date"
                value={emergencia.date}
                onChange={handleChange}
              />
              <button className="emergencia-confirmar" type="submit" id="emergencia-confirmar">CONFIRMAR</button>
            </div>
          </div>
        </form>      
      </div>
    </div>
  );
}
