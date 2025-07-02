from Manejo_consola.Acciones_sistema.accion import Accion

class Agregar_Recuperatorio(Accion):
    def __init__(self, menu, materia):
        super().__init__(menu)
        self.materia_seleccionada = materia

    def agregar_recuperatorio(self, id_nota, valor):
        self.menu.service.agregar_recuperatorio(self.materia_seleccionada.get_id_materia(), id_nota, valor)
        self.menu.interfaz_salida.mostrar_advertencia("recuperatorio_agregado")

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.menu.accion = Seleccionar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        parciales = self.menu.service.obtener_parciales(self.materia_seleccionada)

        if len(parciales) > 0:
            self.menu.interfaz_salida.mostrar_notas(parciales, recu=True, id=True)
            id_nota = self.menu.interfaz_entrada.obtener_entero("ID del parcial a agregar/sobreescribir recuperatorio")
            valor = self.menu.interfaz_entrada.obtener_decimal("Nota del recuperatorio")
            self.agregar_recuperatorio(id_nota, valor)
        else:
            self.menu.interfaz_salida.mostrar_advertencia("sin_notas")
        self.volver()