from Manejo_consola.Acciones_sistema.accion import Accion

class Borrar_Base(Accion):
    def __init__(self, main):
        super().__init__(main)
    
    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)

    def hacer_accion(self):
        confirmacion = self.main.interfaz_entrada.obtener_booleano(
            "¿Estás seguro que querés borrar toda la base?"
        )

        if confirmacion:
            self.main.service.eliminar_base()
            self.main.interfaz_salida.mostrar_advertencia("base_borrada")
        self.volver()