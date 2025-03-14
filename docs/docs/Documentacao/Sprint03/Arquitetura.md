---
title: Arquitetura
slug: arquitetura
sidebar_position: 3
---
# Visão Geral

Este projeto implementa um servidor Flask com integração de WebSockets, utilizando Flask-SocketIO para comunicação em tempo real. O sistema possibilita a leitura e armazenamento de códigos de barras/QR codes em um banco de dados PostgreSQL, com endpoints RESTful para consulta dos dados armazenados.

## Arquitetura do Sistema

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│                 │       │                 │       │                 │
│    Cliente      │◄─────►│    Servidor     │◄─────►│   Banco de      │
│    WebSocket    │       │    Flask        │       │    Dados        │
│                 │       │                 │       │  PostgreSQL     │
└─────────────────┘       └────────┬────────┘       └─────────────────┘
                                   │
                                   │
                          ┌────────▼────────┐
                          │                 │
                          │ Gerenciador de  │
                          │     Filas       │
                          │                 │
                          └─────────────────┘
```

## Componentes Principais

### 1. Servidor Flask

O servidor é inicializado através do arquivo `app.py`, configurado para executar na porta 5000 no ambiente de desenvolvimento. A aplicação utiliza uma estrutura modular com blueprints para organizar as rotas.

```python
# app.py
import os
from app import app, socketio

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host='localhost', port=port, debug=True)
```

A configuração do servidor é realizada no arquivo `__init__.py`, onde são inicializados os principais componentes como:
- Flask-SQLAlchemy para ORM
- Flask-Migrate para gerenciamento de migrações de banco de dados
- Flask-SocketIO para comunicação WebSocket
- Blueprints para rotas REST

### 2. Configuração do Ambiente

O sistema suporta múltiplos ambientes através das classes de configuração definidas em `configuration.py`:

- `ProductionConfig`: Configurações para ambiente de produção
- `DevelopmentConfig`: Configurações para ambiente de desenvolvimento, com modo debug ativado
- `TestingConfig`: Configurações para testes

O banco de dados PostgreSQL é configurado através da variável de ambiente `DATABASE_URL` ou utiliza uma URL padrão quando não especificada.

### 3. Gerenciamento de Filas

Um sistema de filas thread-safe é implementado em `QueueManager.py`, utilizando `threading.Lock` para garantir a integridade das operações concorrentes.

```python
# QueueManager.py (simplificado)
import threading

queue = []
queue_lock = threading.Lock()  

def add_message(message):
    with queue_lock:  
        queue.append(message)

def get_message():
    with queue_lock:
        if queue:
            i = queue[0]
            queue.pop(0)            
            return i
    return None 
```

Este componente atua como intermediário entre as conexões WebSocket e o processamento dos dados recebidos.

### 4. WebSockets

A comunicação em tempo real é implementada utilizando Flask-SocketIO, permitindo conexões de clientes para transmissão de códigos de barras ou QR codes.

```python
# Websockets.py (simplificado)
from flask_socketio import SocketIO
from app.QueueManager import add_message

socketio = SocketIO(cors_allowed_origins="*")  

@socketio.on("connect")
def handle_connect():    
    print("Cliente conectado ao WebSocket")

@socketio.on("message")
def handle_message(data):
    print(f"Mensagem recebida: {data}")
    add_message(data)  

@socketio.on("disconnect")
def handle_disconnect():
    print("Cliente desconectado")
```

As mensagens recebidas via WebSocket são adicionadas à fila de processamento para posterior armazenamento no banco de dados.

### 5. Rotas e Controladores

A aplicação implementa dois grupos principais de rotas:

#### Rota de Códigos (`/codigo`)

Permite o consumo dos códigos da fila e seu armazenamento no banco de dados:

```python
# CodigosRota.py (simplificado)
@codigo_bp.route("/", methods=["POST"])
def post_codigo():
    codigo_controller = CodigosController()
    msg = codigo_controller.get_codigo()
    if msg:
        return f"A rota recebeu: {msg}"
    return "Nenhuma mensagem recebida..."
```

#### Rota de QR Codes (`/qrcode`)

Fornece endpoints para consulta de códigos armazenados:

```python
# QrcodeRouter.py (simplificado)
@qrcode_bp.route("/id=<id>", methods=["GET"])
def getByid_qrcode(id):
    qrcode_controller = QrcodeController()
    res = qrcode_controller.getByid_qrcode(id)  
    return jsonify(res.to_dict()), 200

@qrcode_bp.route("/all", methods=["GET"])
def getAll_qrcode():
    qrcode_controller = QrcodeController()
    lista = qrcode_controller.getAll_qrcode()
    list_dict = [obj.to_dict() for obj in lista]
    return jsonify(list_dict), 200
```

### 6. Modelos de Dados

O modelo de dados principal é definido em `Models.py`, representando a tabela `CodigoBipado` no banco de dados:

```python
# Models.py (simplificado)
from app import db

class CodigoBipado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_barra = db.Column(db.String(250))
        
    def to_dict(self):
        return {
            "id": self.id,
            "codigo_barra": self.codigo_barra
        }
```

## Fluxo de Funcionamento

1. **Recebimento de Códigos via WebSocket**:
   - Um cliente se conecta ao servidor via WebSocket
   - O cliente envia uma mensagem contendo o código escaneado
   - O evento `message` é capturado pelo manipulador `handle_message`
   - O código é adicionado à fila de processamento através do `add_message`

2. **Processamento e Armazenamento**:
   - A rota `/codigo` (método POST) é chamada
   - O controlador `CodigosController` recupera o próximo código da fila com `get_message`
   - O código é armazenado no banco de dados como um novo registro de `CodigoBipado`
   - Uma resposta de confirmação é retornada ao cliente

3. **Consulta de Códigos Armazenados**:
   - A rota `/qrcode/all` retorna todos os códigos armazenados no banco
   - A rota `/qrcode/id=<id>` retorna um código específico pelo seu ID
   - Os resultados são formatados como JSON para consumo pelo cliente

## Migrações do Banco de Dados

O sistema utiliza Flask-Migrate (baseado em Alembic) para gerenciar as migrações do banco de dados. Os arquivos relacionados incluem:
- `alembic.ini`: Configuração do Alembic
- `env.py`: Ambiente de execução das migrações
- `script.py.mako`: Template para scripts de migração

## Dependências

As principais dependências do projeto são:
- Flask 3.1.0
- Flask-SocketIO 5.5.1
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.1.0
- SQLAlchemy 2.0.38
- Psycopg2-binary 2.9.10 (driver PostgreSQL)

## Considerações de Segurança

- A configuração atual permite conexões WebSocket de qualquer origem (`cors_allowed_origins="*"`). Em ambientes de produção, é recomendável restringir as origens permitidas.
- As credenciais do banco de dados estão expostas no código-fonte. É recomendável utilizar variáveis de ambiente ou um sistema de gerenciamento de segredos para armazenar essas informações.

## Utilização

Para iniciar o servidor:

```bash
python app.py
```

Para conectar um cliente WebSocket:
```javascript
const socket = io("http://localhost:5000");
socket.on("connect", () => {
  console.log("Conectado ao servidor WebSocket");
});
socket.emit("message", "123456789"); // Enviar um código de barras
```

Para consultar códigos armazenados:
```bash
# Obter todos os códigos
curl http://localhost:5000/qrcode/all

# Obter um código específico pelo ID
curl http://localhost:5000/qrcode/id=1
```

## Escalabilidade e Melhorias Futuras

- Implementar autenticação para as conexões WebSocket
- Adicionar validação de entrada para os códigos recebidos
- Otimizar o gerenciamento de filas para suportar maior volume de mensagens
- Implementar processamento assíncrono com workers dedicados
- Adicionar testes automatizados para garantir a qualidade do código