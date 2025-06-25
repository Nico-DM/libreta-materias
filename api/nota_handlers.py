from abc import ABC, abstractmethod

class NotaHandler(ABC):
    @abstractmethod
    def ejecutar(self, materia, nota): pass

class ParcialHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_parcial(nota)

class RecuperatorioHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_recuperatorio(nota)

class FinalHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_final(nota)