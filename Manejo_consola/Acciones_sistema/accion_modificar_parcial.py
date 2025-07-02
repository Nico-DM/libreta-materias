from Manejo_consola.Acciones_sistema.accion import Accion

class Modificar_Parcial(Accion):
    def __init__(self, menu, materia, id_nota):
        super().__init__(menu)
        self.materia_seleccionada = materia
        self.parcial_seleccionado = id_nota
        self.OPCIONES_DISPONIBLES = {
            "N": (self.valor_nota_seleccionado, "Nota original"),
            "R": (self.valor_recuperatorio_seleccionado, "Nota del Recuperatorio"),
            "X": (self.volver, "Volver")
        }

    def valor_nota_seleccionado(self):
        from Manejo_consola.Acciones_sistema.accion_modificar_valor_nota import Modificar_Valor_Nota
        self.menu.accion = Modificar_Valor_Nota(self.menu, self.materia_seleccionada, self.parcial_seleccionado)

    def valor_recuperatorio_seleccionado(self):
        from Manejo_consola.Acciones_sistema.accion_modificar_valor_recuperatorio import Modificar_Valor_Recuperatorio
        self.menu.accion = Modificar_Valor_Recuperatorio(self.menu, self.materia_seleccionada, self.parcial_seleccionado)

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_modificar import Modificar
        self.menu.accion = Modificar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        opcion_elegida = self.menu.interfaz_entrada.seleccionar_opcion(self.OPCIONES_DISPONIBLES)
        opcion_elegida[0]()
