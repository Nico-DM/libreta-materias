from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos

class Materia_Es_Promocionable(Evaluacion):
    def __init__(self):
        super().__init__()

    def evaluar(self, datos: Datos) -> bool:
        return datos.get_materia().get_es_promocionable()