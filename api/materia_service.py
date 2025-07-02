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
    
    def obtener_materias(self):
        return self.handlers["materia"].obtener_todas()
    
    def eliminar_materia(self, id: int):
        self.handlers["materia"].eliminar(id)
    
    def modificar_materia(self, id: int, atributo: str, valor):
        self.handlers["materia"].modificar(id, atributo, valor)

    def agregar_parcial(self, id: int, valor: float):
        parcial = Parcial({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
                "valor_recuperatorio": None
            })

        self.handlers["parcial"].agregar(parcial)
        return parcial
    
    def modificar_parcial(self, id: int, atributo: str, valor):
        self.handlers["parcial"].modificar(id, atributo, valor)
    
    def obtener_parciales(self, id_materia):
        materia = self.handlers["materia"].obtener(id_materia)
        return self.handlers["parcial"].obtener_todas_de(materia)
    
    def agregar_final(self, id: int, valor: float):
        final = Final({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
            })

        self.handlers["final"].agregar(final)
        return final
    
    def modificar_final(self, id: int, atributo: str, valor):
        self.handlers["final"].modificar(id, atributo, valor)
    
    def obtener_finales(self, id_materia):
        materia = self.handlers["materia"].obtener(id_materia)
        return self.handlers["final"].obtener_todas_de(materia)

    def agregar_recuperatorio(self, id_materia: int, id_nota: int, valor: float):
        self.handlers["parcial"].agregar_recuperatorio(id_materia, id_nota, valor)
        parcial = self.handlers["parcial"].obtener(id_nota)
        return parcial
    
    def determinar_estado(self, materia):
        id_materia = materia.get_id_materia()
        parciales = self.obtener_parciales(id_materia)
        finales = self.obtener_finales(id_materia)
        return self.determiner.determinar_estado(Datos(materia, parciales, finales))

    def obtener_materia_con_estado(self, id: int):
        try:
            materia = self.handlers["materia"].obtener(id)
            estado = self.determinar_estado(materia)
            return materia, estado
        except Exception as e:
            raise ValueError(f"Materia no encontrada: {str(e)}")

    
    def eliminar_base(self):
        self.handlers["repo"].eliminar_base()
    
    def mover_notas(self, id_vieja: int, id_nueva: int):
        self.handlers["repo"].mover_notas(id_vieja, id_nueva)