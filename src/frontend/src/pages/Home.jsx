import React from 'react';
import { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import SideBar from './components/Sidebar';
import ListaAtual from './components/Lista';
import ProgressBar from './components/ProgressBar';
import styles from '../styles/HomePage.module.css';
import useWebSocketLogs from '../hooks/useWebSocketLogs';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const HomePage = () => {
  const [systemStatus, setSystemStatus] = useState({
    robotStatus: false,
    assemblyStatus: false
  });

  const [medicines, setMedicines] = useState([]);
  const { logs, socket } = useWebSocketLogs('http://localhost:5000');

  useEffect(() => {
    if (!logs.length) return;

    const latestLog = logs[logs.length - 1];
    const { medicineName, progress } = latestLog;

    setMedicines(prevMeds => {
      const exists = prevMeds.some(m => m.name === medicineName);
      const updated = exists
        ? prevMeds.map(med =>
            med.name === medicineName
              ? {
                  ...med,
                  progress,
                }
              : med
          )
        : [...prevMeds, { name: medicineName, progress }];

      if (progress === 100) {
        toast.success(`Montagem concluída: ${medicineName}`);
      }

      return updated;
    });
  }, [logs]);

  const handleTestEvent = () => {
    if (socket) {
      socket.emit('add_medicine', {
        name: `Remédio Teste ${new Date().toLocaleTimeString()}`
      });
    }
  };

  const simulateLog = () => {
    const fakeLog = {
      medicineName: 'Dipirona',
      progress: 80,
      message: 'Simulação local'
    };

    setMedicines(prev => {
      const exists = prev.some(m => m.name === fakeLog.medicineName);
      const updated = exists
        ? prev.map(m => m.name === fakeLog.medicineName ? { ...m, progress: fakeLog.progress } : m)
        : [...prev, { name: fakeLog.medicineName, progress: fakeLog.progress }];

      if (fakeLog.progress === 100) {
        toast.success(`Montagem concluída: ${fakeLog.medicineName}`);
      }

      return updated;
    });
  };

  return (
    <div>
      <h1>Teste de WebSocket</h1>

      <button onClick={handleTestEvent}>Adicionar Medicamento de Teste</button>
      <button onClick={simulateLog}>Simular Evento log</button>

      <div>
        <h2>Logs Recebidos:</h2>
        {logs.map((log, index) => (
          <div key={index}>
            <p>Nome: {log.medicineName}</p>
            <p>Progresso: {log.progress}%</p>
            <p>Mensagem: {log.message}</p>
          </div>
        ))}
      </div>

      <ToastContainer position="top-right" autoClose={3000} hideProgressBar />
    </div>
  );
};

export default HomePage;