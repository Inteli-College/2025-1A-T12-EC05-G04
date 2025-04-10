import threading

# Dicionários para armazenar as filas e seus locks
queues = {
    "robo_status": [],
    "qr_code": [],
    "error_status": [],
    "instrucao": []
}

queue_locks = {
    "robo_status": threading.Lock(),
    "qr_code": threading.Lock(),
    "error_status": threading.Lock(),
    "instrucao": threading.Lock()
}

class QueueManager:
    def __init__(self, queue_name):
        if queue_name not in queues:
            raise ValueError(f"Fila '{queue_name}' não existe.")
        self.queue_name = queue_name
        self.queue = queues[queue_name]
        self.lock = queue_locks[queue_name]

    def add_message(self, message):
        """Adiciona uma mensagem na fila correspondente."""
        with self.lock:
            self.queue.append(message)
            print(f"Fila [{self.queue_name}]:", self.queue)

    def get_all_messages(self):
        """Retorna todas as mensagens da fila."""
        with self.lock:
            return list(self.queue)

    def get_message(self):
        """Remove e retorna a primeira mensagem da fila (FIFO)."""
        with self.lock:
            if self.queue:
                return self.queue.pop(0)
            return None
