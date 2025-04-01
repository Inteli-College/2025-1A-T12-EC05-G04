import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

export default function useWebSocketRoboStatus(url) {
  const [socket, setSocket] = useState(null);
  const [paciente, setPaciente] = useState(null);
  const [medicamentos, setMedicamentos] = useState([]);
  const [logProgresso, setLogProgresso] = useState([]);
  const [status, setStatus] = useState({
    robotStatus: false,
    assemblyStatus: false,
    readyToAssemble: false,
  });

  useEffect(() => {
    const socketInstance = io(url || 'http://localhost:5000', {
      reconnection: true,
      reconnectionAttempts: 5,
      reconnectionDelay: 1000,
    });

    socketInstance.on('connect', () => {
      console.log(' WebSocket conectado');
    });

    socketInstance.on('robo_status_fe', (data) => {
      if (!data?.PacienteId || !data?.Paciente || !data?.Medicamentos || !data?.Logs) {
        console.warn(" Dados incompletos recebidos:", data);
        return;
      }

      // Atualiza status do sistema
      setStatus({
        robotStatus: true,
        assemblyStatus: data.StatusMontagem === 1,
        readyToAssemble: data.StatusMontagem !== 1,
      });

      // Atualiza info do paciente
      setPaciente({
        nome: data.Paciente.nome,
        hc: data.Paciente.hc,
        leito: data.Paciente.leito,
      });

      // Atualiza lista de medicamentos
      setMedicamentos(data.Medicamentos);

      // Atualiza progresso
      const logs = data.Logs.map(log => ({
        medicineName: log.NomeRemedio,
        progress: log.Porcentagem,
      }));
      setLogProgresso(logs);
    });

    socketInstance.on('connect_error', (err) => {
      console.error(' Erro de conexão:', err);
    });

    setSocket(socketInstance);

    return () => socketInstance.disconnect();
  }, [url]);

  return {
    socket,
    paciente,
    medicamentos,
    logProgresso,
    status
  };
}
