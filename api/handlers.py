from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, repo):
        super().__init__()
        self.repo = repo
    
    @abstractmethod
    def agregar(self, objeto): pass

    @abstractmethod
    def obtener(self, id): pass

class MateriaHandler(Handler):
    def agregar(self, objeto):
        self.repo.agregar_materia(objeto)
    
    def obtener(self, id):
        self.repo.obtener_materia(id)

class NotaHandler(Handler):
    @abstractmethod
    def obtener_todas(self, materia): pass

class ParcialHandler(NotaHandler):
    def agregar(self, objeto):
        self.repo.agregar_parcial(objeto)
    
    def obtener(self, id):
        self.repo.obtener_parcial(id)
    
    def obtener_todas(self, materia):
        self.repo.obtener_parciales(materia)
    
    def agregar_recuperatorio(self, id_materia, id_nota, valor):
        self.repo.agregar_recuperatorio(id_materia, id_nota, valor)

class FinalHandler(NotaHandler):
    def agregar(self, objeto):
        self.repo.agregar_final(objeto)
    
    def obtener(self, id):
        self.repo.obtener_final(id)
    
    def obtener_todas(self, materia):
        self.repo.obtener_finales(materia)