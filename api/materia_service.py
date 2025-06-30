from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final
from Dominio.Materias.datos import Datos

class MateriaService:
    def __init__(self, materia_repo, estado_determiner):
        self.repo = materia_repo
        self.determiner = estado_determiner  # solo usado para consulta

    def crear_materia(self, datos: dict):
        materia = Materia(datos)
        self.repo.agregar_materia(materia)
        return materia

    def agregar_parcial(self, id: int, valor: float):
        parcial = Parcial({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
                "valor_recuperatorio": None
            })

        self.repo.agregar_parcial(parcial)
        return parcial
    
    def agregar_final(self, id: int, valor: float):
        final = Final({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
            })

        self.repo.agregar_final(final)
        return final

    def agregar_recuperatorio(self, id_materia: int, id_nota: int, valor: float):
        self.repo.agregar_recuperatorio(id_materia, id_nota, valor)
        parcial = self.repo.obtener_parcial(id_nota)
        return parcial

    def obtener_materia_con_estado(self, id: int):
        materia = self.repo.obtener_materia(id)
        if not materia:
            raise ValueError("Materia no encontrada")
        parciales = self.repo.obtener_parciales(materia)
        finales = self.repo.obtener_finales(materia)
        estado = self.determiner.determinar_estado(Datos(materia, parciales, finales))
        return materia, estado