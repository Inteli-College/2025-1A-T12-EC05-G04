import threading

queue = []
queue_lock = threading.Lock()  

def add_message(message):
    """Adiciona uma mensagem na fila."""
    with queue_lock:  
        queue.append(message)
        print(queue)
        print(f"Mensagem: {message} adicionada a fila")

def get_message():
    """Remove e retorna a primeira mensagem da fila, ou None se estiver vazia."""
    with queue_lock:
        if queue:
            print(queue)
            i = queue[0]
            queue.pop(0)            
            return i
    return None 
