from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos
from Dominio.Materias.parcial import Parcial

class Faltan_Notas_Parcial_o_Recuperatorio(Evaluacion):
    def __init__(self):
        super().__init__()

    def __contar(self, notas: list[Parcial]) -> int:
        return len(notas)

    def __evaluar_cantidad_parciales_mayor_o_igual_min(self, datos: Datos) -> bool:
        notas: list[Parcial] = datos.get_parciales()
        criterio: int = datos.get_materia().get_cant_parciales()

        return self.__contar(notas) >= criterio
    
    def __evaluar_ningun_parcial_desaprobado_sin_recuperatorio(self, datos: Datos) -> bool:
        notas = datos.get_parciales()
        criterio = datos.get_materia().get_nota_min_aprobar()

        for nota in notas:
            if nota.get_valor_nota() < criterio and not nota.get_valor_recuperatorio():
                return True
        
        return False

    def evaluar(self, datos: Datos) -> bool:
        return not (self.__evaluar_cantidad_parciales_mayor_o_igual_min(datos) and self.__evaluar_ningun_parcial_desaprobado_sin_recuperatorio(datos))