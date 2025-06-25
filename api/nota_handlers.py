from abc import ABC, abstractmethod

class NotaHandler(ABC):
    @abstractmethod
    def agregar(self, materia, valor): pass

class ParcialHandler(NotaHandler):
    def agregar(self, materia, valor):
        materia.agregar_parcial(valor)

class RecuperatorioHandler(NotaHandler):
    def agregar(self, materia, id_nota, valor):
        materia.agregar_recuperatorio(valor)

class FinalHandler(NotaHandler):
    def agregar(self, materia, valor):
        materia.agregar_final(valor)