from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Nota(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.ACCIONES_DISPONIBLES = {
            "P": (self.agregar_parcial, "Parcial"),
            "F": (self.agregar_final, "Final"),
            "R": (self.agregar_recuperatorio, "Recuperatorio"),
            "X": (self.volver, "Volver")
        }

    def agregar_parcial(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_parcial import Agregar_Parcial
        self.main.accion = Agregar_Parcial(self.main, self.materia_seleccionada)

    def agregar_final(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_final import Agregar_Final
        self.main.accion = Agregar_Final(self.main, self.materia_seleccionada)

    def agregar_recuperatorio(self):
        from Manejo_consola.Acciones_sistema.accion_agregar_recuperatorio import Agregar_Recuperatorio
        self.main.accion = Agregar_Recuperatorio(self.main, self.materia_seleccionada)

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        opcion_elegida = self.main.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
