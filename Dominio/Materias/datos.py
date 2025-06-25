from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final

class Datos():
    def __init__(self, materia: Materia, parciales: list[Parcial], finales: list[Final]):
        self.__materia: Materia = materia
        self.__parciales: list[Parcial] = parciales
        self.__finales: list[Final] = finales
    
    def set_materia(self, materia: Materia):
        self.__materia = materia
    
    def get_materia(self) -> Materia:
        return self.__materia
    
    def set_parciales(self, parciales: list[Parcial]):
        self.__parciales = parciales
    
    def get_parciales(self) -> list[Parcial]:
        return self.__parciales
    
    def set_finales(self, finales: list[Final]):
        self.__finales = finales
    
    def get_finales(self) -> list[Final]:
        return self.__finales