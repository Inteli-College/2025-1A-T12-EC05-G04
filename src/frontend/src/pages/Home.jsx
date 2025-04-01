import React from "react";
import SideBar from "./components/Sidebar";
import ProgressBar from "./components/ProgressBar";
import useWebSocketRoboStatus from "../hooks/useWebSocketRoboStatus";

const HomePage = () => {
  const {
    paciente,
    medicamentos,
    logProgresso,
    status,
    socket,
  } = useWebSocketRoboStatus("http://localhost:5000");

  const { robotStatus, assemblyStatus, readyToAssemble } = status;

  const StatusButton = ({ label, status }) => {
    const isActive = status;

    return (
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", cursor: "default" }}>
        <span style={{ fontWeight: 600, fontSize: "1.1rem" }}>{label}:</span>
        <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
          <span style={{
            width: "20px",
            height: "20px",
            borderRadius: "50%",
            backgroundColor: isActive ? "#4caf50" : "#ccc"
          }}></span>
          <span style={{ fontSize: "1rem" }}>{isActive ? "Ligado" : "Desligado"}</span>
        </div>
      </div>
    );
  };

  const PatientInfoCard = () => {
    if (!paciente) return null;

    return (
      <div style={{
        backgroundColor: "#e0e0e0",
        padding: "1rem",
        borderRadius: "8px",
        margin: "2rem 0 1rem"
      }}>
        <h3 style={{ fontSize: "1.5rem", fontWeight: "bold", margin: 0 }}>{paciente.nome}</h3>
        <div style={{ fontSize: "1rem", color: "#555" }}>
          {paciente.leito} | {paciente.hc}
        </div>
      </div>
    );
  };

  const MedicationProgressTracker = () => {
    if (!medicamentos.length) {
      return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", padding: "2rem", color: "#888" }}>
          <div style={{
            width: "30px",
            height: "30px",
            border: "4px solid #f3f3f3",
            borderTop: "4px solid #4285f4",
            borderRadius: "50%",
            animation: "spin 1s linear infinite",
            marginBottom: "10px"
          }} />
          <p>Aguardando dados...</p>
        </div>
      );
    }

    return (
      <div style={{ display: "flex", flexDirection: "column", gap: "1.5rem" }}>
        {medicamentos.map((med, index) => {
          const log = logProgresso.find((l) => l.medicineName === med.nome);
          const progress = log?.progress || 0;

          return (
            <div key={index} style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
              <span style={{ minWidth: "180px", fontWeight: 600, fontSize: "0.95rem" }}>{med.nome}</span>
              <ProgressBar name={med.nome} progress={progress} />
            </div>
          );
        })}
      </div>
    );
  };

  const MainContent = () => {
    if (!robotStatus) {
      return (
        <div style={{ padding: "2rem", textAlign: "center", color: "#aaa" }}>
          <p>O robô está desligado. Acione o robô no botão de power localizado na parte traseira da base do braço robótico.</p>
        </div>
      );
    }

    if (robotStatus && !assemblyStatus && readyToAssemble) {
      return (
        <div style={{ padding: "2rem", textAlign: "center", color: "#aaa" }}>
          <p>Parece que o robô não está separando ou montando nenhuma fita médica agora.</p>
          <p>Aprove uma fita para montagem na seção de listas pendentes.</p>
        </div>
      );
    }

    if (robotStatus && assemblyStatus) {
      return (
        <div style={{ padding: "2rem" }}>
          <PatientInfoCard />
          <div style={{ marginTop: "2rem" }}>
            <MedicationProgressTracker />
          </div>
        </div>
      );
    }

    return null;
  };

  return (
    <div style={{ display: "flex", flexDirection: "row", height: "100vh", width: "100vw", backgroundColor: "#fff" }}>
      <div style={{ minWidth: "80px", width: "8vw", backgroundColor: "#f5f5f5", height: "100vh" }}>
        <SideBar />
      </div>
      <div style={{ flex: 1, overflowY: "auto", padding: "0 32px", backgroundColor: "#fff" }}>
        <div style={{ padding: "1rem", borderBottom: "1px solid #e0e0e0", backgroundColor: "#fff" }}>
          <div style={{ display: "flex", gap: "1.5rem", alignItems: "center" }}>
            <StatusButton label="Status" status={robotStatus} />
            {robotStatus && <StatusButton label="Status" status={assemblyStatus} />}
          </div>
        </div>
        <MainContent />
      </div>
    </div>
  );
};

export default HomePage;
