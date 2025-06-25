from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos

class Todos_Parciales_o_Recuperatorio_Aprobados(Evaluacion):
    def __init__(self):
        super().__init__()

    def evaluar(self, datos: Datos) -> bool:
        notas = datos.get_parciales()
        criterio = datos.get_materia().get_nota_min_aprobar()

        for nota in notas:
            if nota.get_valor_nota() < criterio:
                recuperatorio = nota.get_valor_recuperatorio() or 0
                if recuperatorio < criterio:
                    return False
        return len(notas) > 0
