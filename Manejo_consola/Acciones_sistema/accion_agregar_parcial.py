from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Parcial(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_parcial(self, valor):
        self.main.service.agregar_parcial(self.materia_seleccionada.get_id_materia(), valor)
        self.main.interfaz_salida.mostrar_advertencia("parcial_agregado")

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.interfaz_entrada.obtener_decimal("Nota del parcial")
        self.agregar_parcial(valor)
        self.volver()