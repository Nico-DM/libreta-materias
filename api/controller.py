from Dominio.Materias.materia import Materia

class MateriaController:
    def __init__(self, materia_repo, estado_determiner, nota_handlers: dict):
        self.repo = materia_repo
        self.determiner = estado_determiner  # solo usado para consulta
        self.handlers = nota_handlers        # dict con handlers por tipo de nota

    def crear_materia(self, nombre: str):
        materia = Materia(nombre)
        self.repo.guardar(materia)
        return materia

    def agregar_nota(self, nombre: str, tipo: str, nota: float):
        if tipo not in self.handlers:
            raise ValueError(f"Tipo de nota no soportado: {tipo}")

        materia = self.repo.obtener(nombre)
        if not materia:
            raise ValueError("Materia no encontrada")

        self.handlers[tipo].ejecutar(materia, nota)
        self.repo.guardar(materia)
        return materia

    def obtener_materia_con_estado(self, nombre: str):
        materia = self.repo.obtener(nombre)
        if not materia:
            raise ValueError("Materia no encontrada")
        estado = self.determiner.determinar_estado(materia)
        return materia, estado