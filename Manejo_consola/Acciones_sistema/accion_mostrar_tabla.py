import sys
from Manejo_consola.Acciones_sistema.accion import Accion

class Mostrar_Tabla(Accion):
    def __init__(self, menu):
        super().__init__(menu)
        self.ACCIONES_DISPONIBLES = {
            "A": (self.cambiar_a_agregar, "Agregar materia"),
            "B": (self.cambiar_a_borrar_base, "Borrar base"),
            "S": (self.cambiar_a_seleccionar, "Seleccionar materia"),
            "X": (self.salir, "Salir del programa")
        }
    
    def cambiar_a_agregar(self):
        from Manejo_consola.Acciones_sistema.accion_agregar import Agregar
        self.menu.accion = Agregar(self.menu)

    def cambiar_a_borrar_base(self):
        from Manejo_consola.Acciones_sistema.accion_borrar_base import Borrar_Base
        self.menu.accion = Borrar_Base(self.menu)
    
    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.get_id_materia() == id_materia:
                return materia
        return None

    def cambiar_a_seleccionar(self):
        if len(self.materias) > 0: 
            encontrada = False
            while not encontrada:
                id_elegida = self.menu.interfaz_entrada.obtener_entero("ID")
                materia_seleccionada = self.buscar_materia(id_elegida, self.materias)
                if materia_seleccionada:
                    encontrada = True
                    from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
                    self.menu.accion = Seleccionar(self.menu, materia_seleccionada)
                else:
                    self.menu.interfaz_salida.mostrar_advertencia("id_no_disponible")
        else:
            self.menu.interfaz_salida.mostrar_advertencia("sin_materias")

    def salir(self):
        sys.exit(0)

    def hacer_accion(self):
        self.materias = self.menu.service.obtener_materias()
        
        self.menu.interfaz_salida.mostrar_tabla(self.materias, self.menu.service)

        opcion_elegida = self.menu.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
