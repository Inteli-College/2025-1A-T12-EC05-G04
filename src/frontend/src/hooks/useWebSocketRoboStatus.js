import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

export default function useWebSocketRoboStatus(url) {
  const [socket, setSocket] = useState(null);

  // Estados que guardam os dados
  const [paciente, setPaciente] = useState(null);
  const [topic, setTopic] = useState(null);
  const [medicamentos, setMedicamentos] = useState([]); // Dados completos do evento Start
  const [nomeRemedio, setNomeRemedio] = useState(null);
  const [logProgresso, setLogProgresso] = useState([]);  
  const [errorMessage, setErrorMessage] = useState(null);

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

    // Função unificada para processar o payload recebido
    function processReceivedData(data) {
      console.log("Processando payload:", data);
      if (!data || !data.Topico) {
        console.warn("Dados sem Topico:", data);
        return;
      }

      // Variável para log de depuração (apenas para ver o merge dos dados)
      let estadoMensagem = {};

      switch (data.Topico) {
        case 'Start': {
          // Verifica se os dados completos foram enviados
          if (!data.PacienteId || !data.Paciente || !data.Medicamentos || data.StatusMontagem === undefined) {
            console.warn("Tópico Start - Dados incompletos:", data);
            return;
          }
          // Atualiza o status para Start
          setStatus({
            robotStatus: true,
            assemblyStatus: data.StatusMontagem === 1,
            readyToAssemble: data.StatusMontagem !== 1,
          });
          // Atualiza os dados completos
          setPaciente({
            nome: data.Paciente.nome,
            hc: data.Paciente.hc,
            leito: data.Paciente.leito,
          });
          setMedicamentos(data.Medicamentos);
          // Atualiza logs, se enviados (caso venha)
          if (data.Logs && Array.isArray(data.Logs)) {
            const logs = data.Logs.map((log) => ({
              id_montagem: log.IdMontagem, // Se houver, deve vir no payload
              medicineName: log.NomeRemedio,
              progress: log.Porcentagem,
            }));
            setLogProgresso(logs);
          }
          estadoMensagem = {
            paciente: data.Paciente,
            medicamentos: data.Medicamentos,
            status_montagem: data.StatusMontagem,
            topic: data.Topico,
          };
          break;
        }
        case 'Ongoing': {
          // Para Ongoing, exige NomeRemedio, Porcentagem e IdMontagem
          if (!data.NomeRemedio || data.Porcentagem === undefined || !data.IdMontagem) {
            console.warn("Tópico Ongoing - Dados incompletos:", data);
            return;
          }
          setStatus(old => ({
            ...old,
            robotStatus: true,
            assemblyStatus: true, // Já que a montagem está em andamento
            readyToAssemble: false,
          }));
          setNomeRemedio(data.NomeRemedio);
        
          // Atualiza o log com base no IdMontagem
          setLogProgresso(oldLogs => {
            const index = oldLogs.findIndex(log => log.id_montagem === data.IdMontagem);
            if (index >= 0) {
              // Se já existe, atualiza a porcentagem
              const updatedLogs = [...oldLogs];
              updatedLogs[index] = { ...updatedLogs[index], progress: data.Porcentagem };
              return updatedLogs;
            }
            // Se não existe, adiciona novo log
            return [...oldLogs, { id_montagem: data.IdMontagem, medicineName: data.NomeRemedio, progress: data.Porcentagem }];
          });
        
          estadoMensagem = {
            nome_paciente: data.NomeRemedio,
            porcentagem: data.Porcentagem,
            id_montagem: data.IdMontagem,
            topic: data.Topico,
          };
          break;
        }
        case 'Finish': {
          // Para Finish, exige NomeRemedio, Porcentagem e StatusMontagem, e idealmente IdMontagem
          if (!data.NomeRemedio || data.Porcentagem === undefined || data.StatusMontagem === undefined || !data.IdMontagem) {
            console.warn("Tópico Finish - Dados incompletos:", data);
            return;
          }
          setStatus(old => ({
            ...old,
            robotStatus: true,
            assemblyStatus: data.StatusMontagem === 1,
            readyToAssemble: data.StatusMontagem !== 1,
          }));
          setNomeRemedio(data.NomeRemedio);
          setLogProgresso(oldLogs => {
            const id = data.IdMontagem;
            const progress = data.Porcentagem;
            const index = oldLogs.findIndex(log => log.id_montagem === id);
            if (index >= 0) {
              const newLogs = [...oldLogs];
              newLogs[index] = { ...newLogs[index], progress };
              return newLogs;
            }
            return [...oldLogs, { id_montagem: id, medicineName: data.NomeRemedio, progress }];
          });
          estadoMensagem = {
            nome_paciente: data.NomeRemedio,
            porcentagem: data.Porcentagem,
            status_montagem: data.StatusMontagem,
            topic: data.Topico,
          };
          break;
        }
        default:
          console.warn("Tópico desconhecido:", data.Topico);
          return;
      }

      // Atualiza paciente e medicamentos apenas se enviados no payload
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

      // Atualiza o tópico sempre
      setTopic(data.Topico);

      console.log("Estados da mensagem:", estadoMensagem);
    }

    // Função para processar mensagem de erro
    function processErrorMessage(data) {
      console.log("Processando mensagem de erro:", data);
      if (data && data.message) {
        setErrorMessage(data.message);
      } else {
        setErrorMessage("Erro desconhecido no processo do robô.");
      }
    }

    // Escuta os eventos e chama as funções de processamento
    socketInstance.on('robo_status_fe', (data) => {
      console.log('Evento robo_status_fe recebido:', data);
      processReceivedData(data);
    });
    socketInstance.on('montagem_remedio', (data) => {
      console.log('Evento montagem_remedio recebido:', data);
      processReceivedData(data);
    });
    socketInstance.on('error_status', (data) => {
      console.log('Evento error_status recebido:', data);
      processErrorMessage(data);
    });
    socketInstance.on('alive_fe', (data) => {
      console.log('Evento alive_fe recebido:', data);
      // Se o evento vier com a propriedade "message", atualizamos o status do robô para ativo.
      if (data && data.message) {
        setStatus(old => ({ ...old, robotStatus: true }));
        console.log('Status do robô atualizado para ativo. Mensagem:', data.message);
      }
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
    nomeRemedio,
    logProgresso,
    status,
    topic,
    errorMessage,
  };
}
