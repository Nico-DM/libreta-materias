from Dominio.Materias.nota import Nota

class Parcial(Nota):
    def __init__(self, tupla):
        super().__init__(tupla)
        if len(tupla) > 3 and tupla[3]:
            self.__valor_recuperatorio = float(tupla[3])
        else:
            self.__valor_recuperatorio = None

    def get_valor_recuperatorio(self):
        return self.__valor_recuperatorio
    
    def set_valor_recuperatorio(self, valor):
        self.__valor_recuperatorio = valor