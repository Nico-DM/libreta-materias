from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos

class Todos_Parciales_Mayor_o_Igual_Promocion(Evaluacion):
    def __init__(self):
        super().__init__()

    def evaluar(self, datos: Datos) -> bool:
        notas = datos.get_parciales()
        criterio = datos.get_materia().get_nota_min_promocion() or 0

        for nota in notas:
            if nota.get_valor_nota() < criterio:
                return False

        return len(notas) > 0
