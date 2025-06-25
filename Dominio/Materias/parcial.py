from Dominio.Materias.nota import Nota

class Parcial(Nota):
    def __init__(self, datos: dict):
        super().__init__(datos)
        try:
            self.__valor_recuperatorio = float(datos["valor_recuperatorio"])
        except Exception:
            self.__valor_recuperatorio = None

    def get_valor_recuperatorio(self):
        return self.__valor_recuperatorio
    
    def set_valor_recuperatorio(self, valor):
        self.__valor_recuperatorio = valor