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

    // Função para processar os dados recebidos dos eventos
    function processReceivedData(data) {
      console.log("Processando payload:", data);
      if (!data || !data.Topico) {
        console.warn("Dados sem Topico:", data);
        return;
      }

      // Validação condicional conforme o Topico
      switch (data.Topico) {
        case 'Start':
          // Exige dados completos para iniciar
          if (!data.PacienteId || !data.Paciente || !data.Medicamentos || data.StatusMontagem === undefined) {
            console.warn("Tópico Start - Dados incompletos recebidos:", data);
            return;
          }
          break;
        case 'Ongoing':
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

      // Se for o evento "Start", atualiza os estados completos
      if (data.Topico === "Start") {
        setStatus({
          robotStatus: true,
          assemblyStatus: data.StatusMontagem === 1,
          readyToAssemble: data.StatusMontagem !== 1,
        });
        
        // Atualiza paciente e medicamentos somente se vierem no payload
        if (data.Paciente) {
          setPaciente({
            nome: data.Paciente.nome,
            hc: data.Paciente.hc,
            leito: data.Paciente.leito,
          });
        }

        if (data.Medicamentos) {
          setMedicamentos(data.Medicamentos);
        }
        
        // Se os logs vierem, atualiza; se não, não altera o estado.
        if (data.Logs && Array.isArray(data.Logs)) {
          const logs = data.Logs.map((log) => ({
            medicineName: log.NomeRemedio,
            progress: log.Porcentagem,
          }));
          setLogProgresso(logs);
        }
      } else {
        // Para os eventos "Ongoing" e "Finish", atualiza apenas os dados que foram enviados no payload
        // Preserva os estados de paciente e medicamentos, atualizando somente os logs e, se vier StatusMontagem, o status.
        
        // Atualiza ou insere um log para o medicamento conforme NomeRemedio e Porcentagem
        setLogProgresso((oldLogs) => {
          const nome = data.NomeRemedio;
          const porcentagem = data.Porcentagem;
          const index = oldLogs.findIndex((log) => log.medicineName === nome);
          if (index >= 0) {
            const newLogs = [...oldLogs];
            newLogs[index] = { ...newLogs[index], progress: porcentagem };
            return newLogs;
          } else {
            return [...oldLogs, { medicineName: nome, progress: porcentagem }];
          }
        });

        // Atualiza status se StatusMontagem vier no payload
        if (data.StatusMontagem !== undefined) {
          setStatus((oldStatus) => ({
            ...oldStatus,
            assemblyStatus: data.StatusMontagem === 1,
            readyToAssemble: data.StatusMontagem !== 1,
          }));
        }
      }

      // Atualiza o tópico sempre
      setTopic(data.Topico);

      const estadoMensagem = {
        paciente: data.Paciente,
        medicamentos: data.Medicamentos,
        status_montagem: data.StatusMontagem,
        topic: data.Topico,
      };
      console.log("Estados da mensagem:", estadoMensagem);
    }

    // Escuta os eventos e chama a função de processamento
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
