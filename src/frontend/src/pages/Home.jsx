import React, { useEffect } from "react";
import SideBar from "./components/Sidebar";
import ProgressBar from "./components/ProgressBar";
import useWebSocketRoboStatus from "../hooks/useWebSocketRoboStatus";
import ErrorMessage from "./components/ErrorMessage"; // Certifique-se de que esse componente está implementado

const HomePage = () => {
  const {
    paciente,
    medicamentos,
    logProgresso,
    status,
    topic,
    errorMessage,
  } = useWebSocketRoboStatus("http://localhost:5000");

  // Exibe os dados recebidos para depuração
  useEffect(() => {
    console.log("Dados recebidos no HomePage:", {
      paciente,
      medicamentos,
      logProgresso,
      status,
      topic,
      errorMessage,
    });
  }, [paciente, medicamentos, logProgresso, status, topic, errorMessage]);

  const { robotStatus, assemblyStatus } = status;

  // Componente para exibir botões de status com indicador visual
  const StatusButton = ({ label, status }) => (
    <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", cursor: "default" }}>
      <span style={{ fontWeight: 600, fontSize: "1.1rem" }}>{label}:</span>
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
        <span
          style={{
            width: "20px",
            height: "20px",
            borderRadius: "50%",
            backgroundColor: status ? "#4caf50" : "#ccc",
          }}
        ></span>
        <span style={{ fontSize: "1rem" }}>{status ? "Ligado" : "Desligado"}</span>
      </div>
    </div>
  );

  // Exibe informações do paciente, se disponíveis
  const PatientInfoCard = () => {
    if (!paciente) return null;
    return (
      <div
        style={{
          backgroundColor: "#e0e0e0",
          padding: "1rem",
          borderRadius: "8px",
          margin: "2rem 0 1rem",
        }}
      >
        <h3 style={{ fontSize: "1.5rem", fontWeight: "bold", margin: 0 }}>
          {paciente.nome}
        </h3>
        <div style={{ fontSize: "1rem", color: "#555" }}>
          {paciente.leito} | {paciente.hc}
        </div>
      </div>
    );
  };

  // Componente que renderiza a mensagem de status da montagem conforme o tópico
  const AssemblyStatusMessage = () => {
    if (!topic) return null;
    switch (topic) {
      case "Start":
        return (
          <p style={{ fontSize: "1.1rem", color: "#333" }}>
            Iniciando montagem. Aguardando andamento...
          </p>
        );
      case "Ongoing":
        return (
          <p style={{ fontSize: "1.1rem", color: "#333" }}>
            Montagem em andamento.
          </p>
        );
      case "Finish":
        return (
          <p style={{ fontSize: "1.1rem", color: "#333" }}>
            Montagem finalizada!
          </p>
        );
      default:
        return null;
    }
  };

  // Componente que renderiza a lista de medicamentos com barra de progresso para cada item.
  const MedicationProgressTracker = () => {
    if (!medicamentos.length) {
      return (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            padding: "2rem",
            color: "#888",
          }}
        >
          <div
            style={{
              width: "30px",
              height: "30px",
              border: "4px solid #f3f3f3",
              borderTop: "4px solid #4285f4",
              borderRadius: "50%",
              animation: "spin 1s linear infinite",
              marginBottom: "10px",
            }}
          />
          <p>Aguardando dados...</p>
        </div>
      );
    }

    return (
      <div style={{ display: "flex", flexDirection: "column", gap: "1.5rem" }}>
        {medicamentos.map((med, index) => {
          // Se o objeto med tiver id_montagem, buscamos log pela comparação com id_montagem;
          // se não, buscamos pelo nome (medicineName).
          const log = med.id_montagem
            ? logProgresso.find((l) => l.id_montagem === med.id_montagem)
            : logProgresso.find((l) => l.medicineName === med.nome);
          const progress = log ? log.progress : 0;
          return (
            <div key={index} style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
              <span style={{ minWidth: "180px", fontWeight: 600, fontSize: "0.95rem" }}>
                {med.nome}
              </span>
              <ProgressBar name={med.nome} progress={progress} />
            </div>
          );
        })}
      </div>
    );
    
  };

  // Componente principal que define o conteúdo da tela com base no status do robô e montagem
  const MainContent = () => {
    if (!robotStatus) {
      return (
        <div style={{ padding: "2rem", textAlign: "center", color: "#aaa" }}>
          <p>
            O robô está desligado. Acione o robô no botão de power localizado na parte traseira da base do braço robótico.
          </p>
        </div>
      );
    }

    switch (topic) {
      case "Start":
        return (
          <div style={{ padding: "2rem" }}>
            <AssemblyStatusMessage />
            <PatientInfoCard />
            <MedicationProgressTracker />
          </div>
        );
      case "Ongoing":
        return (
          <div style={{ padding: "2rem" }}>
            <AssemblyStatusMessage />
            <PatientInfoCard />
            <MedicationProgressTracker />
          </div>
        );
      case "Finish":
        return (
          <div style={{ padding: "2rem" }}>
            <AssemblyStatusMessage />
            <PatientInfoCard />
            <MedicationProgressTracker />
          </div>
        );
      default:
        return (
          <div style={{ padding: "2rem", textAlign: "center", color: "#aaa" }}>
            <p>Aguardando dados...</p>
          </div>
        );
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        height: "100vh",
        width: "100vw",
        backgroundColor: "#fff",
      }}
    >
      <div
        style={{
          minWidth: "80px",
          width: "8vw",
          backgroundColor: "#f5f5f5",
          height: "100vh",
        }}
      >
        <SideBar />
      </div>
      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "0 32px",
          backgroundColor: "#fff",
        }}
      >
        <div
          style={{
            padding: "1rem",
            borderBottom: "1px solid #e0e0e0",
            backgroundColor: "#fff",
          }}
        >
          <div style={{ display: "flex", gap: "1.5rem", alignItems: "center" }}>
            <StatusButton label="Robô" status={robotStatus} />
            <StatusButton label="Montagem" status={assemblyStatus} />
          </div>
        </div>
        <ErrorMessage message={errorMessage} />
        <MainContent />
      </div>
    </div>
  );
};

export default HomePage;
