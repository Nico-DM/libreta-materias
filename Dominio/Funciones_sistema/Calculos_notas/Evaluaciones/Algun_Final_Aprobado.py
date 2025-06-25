from Dominio.Funciones_sistema.Calculos_notas.evaluacion import Evaluacion
from Dominio.Materias.datos import Datos

class Algun_Final_Aprobado(Evaluacion):
    def __init__(self):
        super().__init__()

    def evaluar(self, datos: Datos) -> bool:
        notas = datos.get_finales()
        criterio = datos.get_materia().get_nota_min_aprobar()

        for nota in notas:
            if nota.get_valor_nota() >= criterio:
                return True

        return False
