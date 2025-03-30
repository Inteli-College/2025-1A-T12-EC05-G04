# HomePage

# Integração WebSocket - Back-End e Front-End

## 1. Comportamento no Back-End

A seguir, são apresentados os principais eventos do servidor WebSocket, implementado com `Flask-SocketIO`, responsáveis pela comunicação com o front-end.

### 1.1. Eventos de Conexão e Desconexão

```python
@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")
```

Descrição:

- Conexão (connect):
Quando um cliente se conecta ao servidor WebSocket, a função handle_connect é executada e imprime uma mensagem no console.

- Desconexão (disconnect):
Quando o cliente se desconecta, handle_disconnect é acionada e registra o evento no console.

### 1.2. Evento Personalizado: log

```python
@socketio.on("log")
def handle_log(data):
    try:
        data = parse_socketio_payload(data)
        if isinstance(data, str):
            data = json.loads(data)
        print("[WS] Evento 'log' recebido:", data)

        if not isinstance(data, dict):
            print(" Ignorado: payload não é dicionário")
            return
        if "medicineName" not in data or "progress" not in data:
            print(" Ignorado: campos obrigatórios ausentes")
            return

        socketio.emit("log", data)
    except Exception as e:
        print("❌ Erro ao processar 'log':", str(e))

```

#### Função auxiliar

```python

def parse_socketio_payload(raw):
    """Extrai e decodifica o JSON do frame socket.io."""
    try:
        if isinstance(raw, str) and raw.startswith("42"):
            payload = raw[2:]  # remove o "42"
            return json.loads(payload)[1]  # [event, data]
        elif isinstance(raw, dict):
            return raw
        return None
    except Exception as e:
        print("❌ Erro ao parsear payload socket.io:", e)
        return None
```

Descrição:

- Parse do Payload: A função parse_socketio_payload extrai e decodifica os dados recebidos. Se o payload começar com "42", remove esse prefixo e trata o restante como JSON válido.

- Validação: O servidor garante que os dados recebidos sejam um dicionário e contenham os campos medicineName e progress.

- Reemissão: Caso os dados sejam válidos, o evento log é retransmitido a todos os clientes conectados.

## 2. Comportamento no Front-End
### 2.1. Hook: useWebSocketLogs

```javascript
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
```

Descrição:

- Estabelecimento da conexão: A conexão é feita com o back-end usando socket.io-client.

- Eventos escutados:

   - `connect`: Confirma a conexão.

   - `log`: Atualiza a lista de logs com base em medicineName.

   - `connect_error`: Captura falhas de conexão.

- Gerenciamento de estado: Os dados recebidos são armazenados em logs e atualizados dinamicamente conforme chegam.

### 2.2. Componente: HomePage

Comportamentos importantes:

- Gerencia os estados do sistema:

   - `robotStatus` (robô ligado)

   - `assemblyStatus` (montagem ativa)

   - `medicines` (lista de medicamentos sendo montados)

   - `connectionError` (problemas na conexão WebSocket)

- Reação à conexão WebSocket: Usa o hook useWebSocketLogs para escutar o evento log e renderiza componentes ProgressBar com os dados recebidos.

- Lógica adicional:

   - Simulação de progresso a cada segundo quando montagem está ativa.

   - Permite adicionar novos medicamentos à lista.

   - Interface muda dinamicamente de acordo com os status.

### Print tela HomePage

<div align="center">
![Tela HomePage](/../../media/homepageS4.png)
<sub>Fonte: Material produzido pelos autores (2025).</sub>
</div>