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
      console.log('Log recebido no frontend:', data);

      if (!data?.medicineName || typeof data.progress !== 'number') return;

      setLogs((prev) => {
        const updated = [...prev];
        const index = updated.findIndex((log) => log.medicineName === data.medicineName);

        if (index !== -1) updated[index] = data;
        else updated.push(data);

        return updated;
      });
    });

    newSocket.on('connect_error', (err) => {
      console.error('Erro de conexão WebSocket:', err);
    });

    setSocket(newSocket);

    return () => newSocket.disconnect();
  }, [url]);

  return { logs, socket };
}
