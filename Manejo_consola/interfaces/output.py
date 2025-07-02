from abc import ABC, abstractmethod

class Interfaz_Output(ABC):
    def __init__(self):
        super().__init__()
        self.ADVERTENCIAS = {
            "id_no_disponible": "No se ingresó una ID disponible. Intente de nuevo.",
            "no_entero": "No se ingresó un número entero. Intente de nuevo.",
            "no_decimal": "No se ingresó un número decimal. Intente de nuevo.",
            "no_booleano": "No se ingresó 'S' (sí) o 'N' (no). Intente de nuevo.",
            "opcion_invalida": "No se ingresó una acción disponible. Intente de nuevo.",
            "sin_notas": "No se encontraron notas.",
            "sin_materias": "No se encontraron materias.",
            "materia_agregada": "Se agregó la materia correctamente.",
            "materia_eliminada": "Se eliminó la materia correctamente.",
            "parcial_agregado": "Se agregó el parcial correctamente.",
            "final_agregado": "Se agregó el final correctamente.",
            "recuperatorio_agregado": "Se agregó/sobreescribió el recuperatorio correctamente.",
            "base_borrada": "Se borraron todas las materias y sus notas."
        }

    @abstractmethod
    def mostrar_advertencia(self, id_advertencia):
        pass

    @abstractmethod
    def mostrar_tabla(self, materias, service):
        pass

    @abstractmethod
    def mostrar_notas(self, notas, recu=False, id=False):
        pass

    @abstractmethod
    def mostrar_info_materia(self, materia_seleccionada, service):
        pass