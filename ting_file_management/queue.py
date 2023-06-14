from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []  # inicializando uma array

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)  # o append adiciona ao fim da fila

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)  # remove o primeiro da fila (índice 0)

    def search(self, index):
        if index >= 0 and index < len(self.queue):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")

    # método que será usado no módulo file_process:
    def is_in_queue(self, path_file):
        for index in range(len(self.queue)):
            if self.queue[index]["nome_do_arquivo"] == path_file:  # obs1
                return True
        return False

# obs1: no req3, o nome do arquivo será armazenado na chave "nome_do_arquivo"
