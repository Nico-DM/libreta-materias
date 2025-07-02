from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos
from typing import Sequence

"""
Cursando: Faltan_Notas_Parcial_o_Recuperatorio
Promocionado: Materia_Es_Promocionable, Todos_Parciales_Mayor_o_Igual_Promocion
Aprobado: Algun_Final_Aprobado
Regularizado: Todos_Parciales_o_Recuperatorio_Aprobados, Cantidad_Finales_Menor_Max
Desaprobado: else
"""

class Determinador_Estado():
    def __init__(self,
                evaluaciones_cursando: Sequence[Evaluacion],
                evaluaciones_promociono: Sequence[Evaluacion],
                evaluaciones_aprobo: Sequence[Evaluacion],
                evaluaciones_regularizo: Sequence[Evaluacion]):
        self.__evaluaciones_cursando: list[Evaluacion] = list(evaluaciones_cursando)
        self.__evaluaciones_promociono: list[Evaluacion] = list(evaluaciones_promociono)
        self.__evaluaciones_aprobo: list[Evaluacion] = list(evaluaciones_aprobo)
        self.__evaluaciones_regularizo: list[Evaluacion] = list(evaluaciones_regularizo)

    def __evaluar_serie(self, evaluaciones: list[Evaluacion], datos: Datos) -> bool:
        for evaluacion in evaluaciones:
            if not evaluacion.evaluar(datos):
                return False
        return True
    
    def determinar_estado(self, datos) -> Estado:
        if self.__evaluar_serie(self.__evaluaciones_promociono, datos):
            return Estado.PROMOCIONADO
        elif self.__evaluar_serie(self.__evaluaciones_aprobo, datos):
            return Estado.APROBADO
        elif self.__evaluar_serie(self.__evaluaciones_regularizo, datos):
            return Estado.REGULARIZADO
        elif self.__evaluar_serie(self.__evaluaciones_cursando, datos):
            return Estado.CURSANDO
        else:
            return Estado.DESAPROBADO
