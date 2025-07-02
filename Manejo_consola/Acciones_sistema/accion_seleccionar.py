from Manejo_consola.Acciones_sistema.accion import Accion
from Dominio.Materias.materia import Materia

class Seleccionar(Accion):
    def __init__(self, menu, materia: Materia):
        super().__init__(menu)
        self.materia_seleccionada: Materia = materia
        self.ACCIONES_DISPONIBLES = {
            "A": (self.cambiar_a_agregar_nota, "Agregar nota"),
            "M": (self.cambiar_a_modificar, "Modificar materia"),
            "E": (self.cambiar_a_eliminar, "Eliminar materia"),
            "X": (self.volver, "Volver")
        }

    def cambiar_a_agregar_nota(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_nota import Agregar_Nota
        self.menu.accion = Agregar_Nota(self.menu, self.materia_seleccionada)

    def cambiar_a_modificar(self):
        from Manejo_consola.Acciones_sistema.accion_modificar import Modificar
        self.menu.accion = Modificar(self.menu, self.materia_seleccionada)

    def cambiar_a_eliminar(self):
        from Manejo_consola.Acciones_sistema.accion_eliminar import Eliminar
        self.menu.accion = Eliminar(self.menu, self.materia_seleccionada)

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.menu.accion = Mostrar_Tabla(self.menu)

    def buscar_materia(self, id_materia, materias: list[Materia]) -> Materia:
        for materia in materias:
            if materia.get_id_materia() == id_materia:
                return materia
        return self.materia_seleccionada

    def hacer_accion(self):
        materias = self.menu.service.obtener_materias()

        self.materia_seleccionada: Materia = self.buscar_materia(self.materia_seleccionada.get_id_materia(), materias)

        self.menu.interfaz_salida.mostrar_info_materia(self.materia_seleccionada, self.menu.service)

        opcion_elegida = self.menu.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
