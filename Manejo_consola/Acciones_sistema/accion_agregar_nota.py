from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Nota(Accion):
    def __init__(self, menu, materia):
        super().__init__(menu)
        self.materia_seleccionada = materia
        self.ACCIONES_DISPONIBLES = {
            "P": (self.agregar_parcial, "Parcial"),
            "F": (self.agregar_final, "Final"),
            "R": (self.agregar_recuperatorio, "Recuperatorio"),
            "X": (self.volver, "Volver")
        }

    def agregar_parcial(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_parcial import Agregar_Parcial
        self.menu.accion = Agregar_Parcial(self.menu, self.materia_seleccionada)

    def agregar_final(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_final import Agregar_Final
        self.menu.accion = Agregar_Final(self.menu, self.materia_seleccionada)

    def agregar_recuperatorio(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_recuperatorio import Agregar_Recuperatorio
        self.menu.accion = Agregar_Recuperatorio(self.menu, self.materia_seleccionada)

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.menu.accion = Seleccionar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        opcion_elegida = self.menu.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
