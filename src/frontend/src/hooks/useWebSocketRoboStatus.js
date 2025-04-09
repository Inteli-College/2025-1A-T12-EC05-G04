import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

export default function useWebSocketRoboStatus(url) {
  const [socket, setSocket] = useState(null);

  // Estados que guardam os dados
  const [paciente, setPaciente] = useState(null);
  const [topic, setTopic] = useState(null);
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
      console.log('WebSocket conectado');
    });

    function processReceivedData(data) {
      console.log("Processando payload:", data);

      if (!data || !data.Topico) {
        console.warn("Dados incompletos recebidos:", data);
        return;
      }

      // Validação condicional conforme o Topico
      switch (data.Topico) {
        case 'Start':
          // Exige que venham Paciente, Medicamentos, etc.
          if (!data.PacienteId || !data.Paciente || !data.Medicamentos || data.StatusMontagem === undefined) {
            console.warn("Tópico Start - Dados incompletos recebidos:", data);
            return;
          }
          break;

        case 'Ongoing':
          // Só exige NomeRemedio e Porcentagem
          if (!data.NomeRemedio || data.Porcentagem === undefined) {
            console.warn("Tópico Ongoing - Dados incompletos recebidos:", data);
            return;
          }
          break;

        case 'Finish':
          if (!data.NomeRemedio || data.Porcentagem === undefined || data.StatusMontagem === undefined) {
            console.warn("Tópico Finish - Dados incompletos recebidos:", data);
            return;
          }
          break;

        default:
          console.warn("Tópico desconhecido:", data.Topico);
          return;
      }

      // Atualização de status: se StatusMontagem não veio, mantém o antigo
      setStatus(old => ({
        ...old,
        robotStatus: true,
        assemblyStatus: data.StatusMontagem !== undefined
          ? (data.StatusMontagem === 1)
          : old.assemblyStatus,
        readyToAssemble: data.StatusMontagem !== undefined
          ? (data.StatusMontagem !== 1)
          : old.readyToAssemble,
      }));

      // Se veio Paciente, atualiza; se não vier, mantém o anterior
      if (data.Paciente) {
        setPaciente({
          nome: data.Paciente.nome,
          hc: data.Paciente.hc,
          leito: data.Paciente.leito,
        });
      }

      // Se veio Medicamentos, atualiza; senão, mantém os anteriores
      if (data.Medicamentos) {
        setMedicamentos(data.Medicamentos);
      }

      // Se veio Logs, processa e substitui; se não vier, mantém
      if (data.Logs && Array.isArray(data.Logs)) {
        const logs = data.Logs.map((log) => ({
          medicineName: log.NomeRemedio,
          progress: log.Porcentagem,
        }));
        setLogProgresso(logs);
      }

      // Atualiza o tópico
      setTopic(data.Topico);

      console.log("Estados atualizados (merge parcial):", {
        paciente: data.Paciente,
        medicamentos: data.Medicamentos,
        status: data.StatusMontagem,
        topic: data.Topico,
      });
    }

    // Escuta os eventos e processa os dados
    socketInstance.on('robo_status_fe', (data) => {
      console.log('Evento robo_status_fe recebido:', data);
      processReceivedData(data);
    });

    socketInstance.on('montagem_remedio', (data) => {
      console.log('Evento montagem_remedio recebido:', data);
      processReceivedData(data);
    });

    socketInstance.on('connect_error', (err) => {
      console.error('Erro de conexão:', err);
    });

    setSocket(socketInstance);

    return () => socketInstance.disconnect();
  }, [url]);

  return {
    socket,
    paciente,
    medicamentos,
    logProgresso,
    status,
    topic,
  };
}
