from Manejo_consola.Acciones_sistema.accion import Accion

class Modificar_Final(Accion):
    def __init__(self, menu, materia, id_nota):
        super().__init__(menu)
        self.materia_seleccionada = materia
        self.id_nota = id_nota

    def cambiar_a_seleccionar(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.menu.accion = Seleccionar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.menu.interfaz_entrada.obtener_decimal("Nota del final")
        self.menu.service.modificar_final(self.id_nota, "valor_nota", valor)
        self.cambiar_a_seleccionar()