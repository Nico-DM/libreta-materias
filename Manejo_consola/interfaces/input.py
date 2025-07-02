from abc import ABC, abstractmethod

class Interfaz_Input(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def obtener_entero(self, entero_a_obtener):
        pass

    @abstractmethod
    def obtener_decimal(self, decimal_a_obtener):
        pass

    @abstractmethod
    def obtener_cadena(self, cadena_a_obtener):
        pass

    @abstractmethod
    def obtener_booleano(self, booleano_a_obtener):
        pass

    @abstractmethod
    def seleccionar_opcion(self, opciones_disponibles):
        pass