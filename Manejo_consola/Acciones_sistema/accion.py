from abc import ABC, abstractmethod

class Accion(ABC):
    def __init__(self, menu):
        super().__init__()
        self.menu = menu

    @abstractmethod
    def hacer_accion(self):
        pass