from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final
from Dominio.Materias.datos import Datos

class MateriaService:
    def __init__(self, estado_determiner, handlers):
        self.determiner = estado_determiner
        self.handlers = handlers

    def crear_materia(self, datos: dict):
        materia = Materia(datos)
        self.handlers["materia"].agregar(materia)
        return materia

    def agregar_parcial(self, id: int, valor: float):
        parcial = Parcial({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
                "valor_recuperatorio": None
            })

        self.handlers["parcial"].agregar(parcial)
        return parcial
    
    def agregar_final(self, id: int, valor: float):
        final = Final({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
            })

        self.handlers["final"].agregar(final)
        return final

    def agregar_recuperatorio(self, id_materia: int, id_nota: int, valor: float):
        self.handlers["parcial"].agregar_recuperatorio(id_materia, id_nota, valor)
        parcial = self.handlers["parcial"].obtener(id_nota)
        return parcial

    def obtener_materia_con_estado(self, id: int):
        materia = self.handlers["materia"].obtener(id)
        if not materia:
            raise ValueError("Materia no encontrada")
        parciales = self.handlers["parcial"].obtener_todas(materia)
        finales = self.handlers["final"].obtener_todas(materia)
        estado = self.determiner.determinar_estado(Datos(materia, parciales, finales))
        return materia, estado