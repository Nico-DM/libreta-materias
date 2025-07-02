from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Final(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia

    def agregar_final(self, valor):
        self.main.service.agregar_final(self.materia_seleccionada.get_id_materia(), valor)
        self.main.interfaz_salida.mostrar_advertencia("final_agregado")

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def hacer_accion(self):
        valor = self.main.interfaz_entrada.obtener_decimal("Nota del final")
        self.agregar_final(valor)
        self.volver()