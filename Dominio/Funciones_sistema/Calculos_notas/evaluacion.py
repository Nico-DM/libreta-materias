from abc import ABC, abstractmethod

class Evaluacion(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def evaluar(self, datos) -> bool:
        pass