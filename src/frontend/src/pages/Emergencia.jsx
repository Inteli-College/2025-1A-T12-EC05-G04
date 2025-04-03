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
    date: getTodayDate(),
  });

  const usuarioLogado = JSON.parse(localStorage.getItem("usuario"));
  const [remediosDisponiveis, setRemediosDisponiveis] = useState([]);
  const [remediosSelecionados, setRemediosSelecionados] = useState([]);

  // MOCKANDO USUÁRIO LOGADO (para teste)
  useEffect(() => {
    const usuarioMock = {
      id: 4,
      nome: "Roberto",
      email: "roberto@teste.com",
      cpf: "1222233444"
    };
    localStorage.setItem("usuario", JSON.stringify(usuarioMock));
  }, []);

  // Busca os remédios disponíveis
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

    // Atualiza o nome do paciente com base no usuário logado (se necessário, mas neste caso não mandamos o nome do enfermeiro)
    // Você pode remover essa parte se o nome do enfermeiro não for necessário para o envio.
  }, []);

  // Função que dispara quando o campo HC perde o foco
  const handleHcBlur = async () => {
    if (emergencia.hc.trim() !== "") {
      try {
        // Supondo que exista um endpoint que valida o HC e retorna os dados do paciente
        const response = await axios.get(`http://localhost:5000/pacientes/validar/${emergencia.hc}`);
        // Se paciente for encontrado, atualize os campos de nome e leito
        if (response.data && response.data.nome && response.data.leito) {
          setEmergencia((prev) => ({
            ...prev,
            nomePaciente: response.data.nome,
            leito: response.data.leito
          }));
        } else {
          // Caso não encontre, limpar os campos
          setEmergencia((prev) => ({
            ...prev,
            nomePaciente: '',
            leito: ''
          }));
          alert("Paciente não encontrado com esse HC.");
        }
      } catch (error) {
        console.error("Erro ao validar HC:", error);
        alert("Erro ao validar HC.");
      }
    }
  };

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

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const dadosFormulario = {
      ...emergencia,
      enfermeiro_id: usuarioLogado?.id,
      remedios: remediosSelecionados.map((r) => ({
        remedioID: r.id_remedio, // mapeia a chave para "remedioID"
        quantidade: r.quantidade,
      })),
    };
  
    console.log("Dados a enviar:", dadosFormulario);
  
    try {
      const response = await axios.post(
        "http://localhost:5000/lista/emergencia/forms",
        dadosFormulario,
        { headers: { "Content-Type": "application/json" } }
      );
      console.log("Formulário enviado com sucesso:", response.data);
      // Exiba mensagem de sucesso ou redirecione
    } catch (error) {
      console.error("Erro ao enviar dados:", error.response?.data || error.message);
      // Exiba mensagem de erro
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
              {/* Apenas o HC é editável */}
              <input 
                type="text" 
                id="hc"
                name="hc"
                placeholder="Informe o HC do paciente"
                value={emergencia.hc}
                onChange={handleChange}
                onBlur={handleHcBlur}
              />
              {/* Esses campos serão preenchidos automaticamente */}
              <input 
                type="text" 
                id="nome-paciente"
                name="nomePaciente"
                placeholder="Nome do paciente"
                value={emergencia.nomePaciente}
                readOnly
              />
              <input 
                type="text"
                id="leito" 
                name="leito"
                placeholder="Leito"
                value={emergencia.leito}
                readOnly
              />
              {/* Removido o campo de enfermeiro, pois o ID será enviado */}
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
