// hooks/useWebSocketLogs.js
import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

export default function useWebSocketLogs(url) {
  const [logs, setLogs] = useState([]);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const safeUrl = (url || 'http://localhost:5000').trim();

    const newSocket = io(safeUrl, {
      reconnection: true,
      reconnectionAttempts: 5,
      reconnectionDelay: 1000,
    });

    newSocket.on('connect', () => {
      console.log('WebSocket conectado');
    });

    newSocket.on('log', (data) => {
      console.log('⚡ Evento log recebido');
      console.log('📦 Dados do log:', data);
      console.log('🧪 Tipo:', typeof data);
      console.log('🔑 Campos:', Object.keys(data));

      setLogs(prev => {
        const isDuplicate = prev.some(
          log => JSON.stringify(log) === JSON.stringify(data)
        );
        console.log(isDuplicate ? '⛔ Duplicado - ignorado' : '✅ Adicionado aos logs');
        return isDuplicate ? prev : [...prev, data];
      });
    });

    newSocket.on('connect_error', (err) => {
      console.error('Erro de conexão WebSocket:', err);
    });

    setSocket(newSocket);
    console.log('📡 Socket criado:', newSocket);

    return () => newSocket.disconnect();
  }, [url]);

  return { logs, socket };
}
