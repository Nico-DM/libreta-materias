from Manejo_consola.Acciones_sistema.accion import Accion

class Eliminar(Accion):
    def __init__(self, main, materia):
        super().__init__(main)
        self.materia_seleccionada = materia
    
    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def eliminar_y_mostrar_tabla(self, ID_materia_seleccionada):
        self.main.service.eliminar_materia(ID_materia_seleccionada)
        self.main.interfaz_salida.mostrar_advertencia("materia_eliminada")
        from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)

    def hacer_accion(self):
        confirmacion = self.main.interfaz_entrada.obtener_booleano(
            f"¿Estás seguro que querés eliminar la materia {self.materia_seleccionada.get_nombre_materia()} y todos sus parciales/finales asociados?"
        )

        if confirmacion:
            self.eliminar_y_mostrar_tabla(self.materia_seleccionada.get_id_materia())
        else:
            self.volver()