from Manejo_consola.Acciones_sistema.accion import Accion

class Borrar_Base(Accion):
    def __init__(self, menu):
        super().__init__(menu)
    
    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.menu.accion = Mostrar_Tabla(self.menu)

    def hacer_accion(self):
        confirmacion = self.menu.interfaz_entrada.obtener_booleano(
            "¿Estás seguro que querés borrar toda la base?"
        )

        if confirmacion:
            self.menu.service.eliminar_base()
            self.menu.interfaz_salida.mostrar_advertencia("base_borrada")
        self.volver()