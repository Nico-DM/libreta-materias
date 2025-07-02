from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Parcial(Accion):
    def __init__(self, menu, materia):
        super().__init__(menu)
        self.materia_seleccionada = materia

    def agregar_parcial(self, valor):
        self.menu.service.agregar_parcial(self.materia_seleccionada.get_id_materia(), valor)
        self.menu.interfaz_salida.mostrar_advertencia("parcial_agregado")

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.menu.accion = Seleccionar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.menu.interfaz_entrada.obtener_decimal("Nota del parcial")
        self.agregar_parcial(valor)
        self.volver()