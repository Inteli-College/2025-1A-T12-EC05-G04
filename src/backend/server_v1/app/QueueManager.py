import threading

queue = []
queue_lock = threading.Lock()  

class QueueRoboStatus:
    def __init__(self):
        pass

    def add_message(self, message):
        """Adiciona uma mensagem na fila RoboStatus."""
        with queue_lock:  
            queue.append(message)
            print(queue)
            print(f"Mensagem: {message} adicionada a fila RoboStatus")

    def get_message(self):
        """Remove e retorna a primeira mensagem da fila RoboStatus, ou None se estiver vazia."""
        with queue_lock:
            if queue:
                print(queue)
                i = queue[0]
                queue.pop(0)            
                return i
        return None 
    

class QueueQrCode:
    def __init__(self):
        pass

    def add_message(self, message):
        """Adiciona uma mensagem na fila do QrCode."""
        with queue_lock:  
            queue.append(message)
            print(queue)
            print(f"Mensagem: {message} adicionada a fila QrCode")

    def get_message(self):
        """Remove e retorna a primeira mensagem da fila QrCode, ou None se estiver vazia."""
        with queue_lock:
            if queue:
                print(queue)
                i = queue[0]
                queue.pop(0)            
                return i
        return None 
    

class QueueErrorStatus:
    def __init__(self):
        pass

    def add_message(self, message):
        """Adiciona uma mensagem na fila ErroStatus."""
        with queue_lock:  
            queue.append(message)
            print(queue)
            print(f"Mensagem: {message} adicionada a fila ErrorStatus")

    def get_message(self):
        """Remove e retorna a primeira mensagem da fila ErrorStatus, ou None se estiver vazia."""
        with queue_lock:
            if queue:
                print(queue)
                i = queue[0]
                queue.pop(0)            
                return i
        return None 
    

