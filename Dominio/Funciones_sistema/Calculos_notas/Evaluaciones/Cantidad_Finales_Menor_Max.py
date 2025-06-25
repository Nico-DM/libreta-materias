from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos
from Dominio.Materias.final import Final

class Cantidad_Finales_Menor_Max(Evaluacion):
    def __init__(self):
        super().__init__()

    def __contar(self, notas: list[Final]) -> int:
        return len(notas)
    
    def calcular_intentos_restantes(self, notas: list[Final], cantidad_maxima: int) -> int:
        return cantidad_maxima - self.__contar(notas)

    def evaluar(self, datos: Datos) -> bool:
        notas: list[Final] = datos.get_finales()
        criterio: int = datos.get_materia().get_cant_veces_final_rendible()

        return self.calcular_intentos_restantes(notas, criterio) > 0
