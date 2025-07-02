import sys
from Manejo_consola.Acciones_sistema.accion import Accion

class Mostrar_Tabla(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.ACCIONES_DISPONIBLES = {
            "A": (self.cambiar_a_agregar, "Agregar materia"),
            "B": (self.cambiar_a_borrar_base, "Borrar base"),
            "S": (self.cambiar_a_seleccionar, "Seleccionar materia"),
            "X": (self.salir, "Salir del programa")
        }
    
    def cambiar_a_agregar(self):
        from Manejo_consola.Acciones_sistema.accion_agregar import Agregar
        self.main.accion = Agregar(self.main)

    def cambiar_a_borrar_base(self):
        from Manejo_consola.Acciones_sistema.accion_borrar_base import Borrar_Base
        self.main.accion = Borrar_Base(self.main)
    
    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.get_id_materia() == id_materia:
                return materia
        return None

    def cambiar_a_seleccionar(self):
        if len(self.materias) > 0: 
            encontrada = False
            while not encontrada:
                id_elegida = self.main.interfaz_entrada.obtener_entero("ID")
                materia_seleccionada = self.buscar_materia(id_elegida, self.materias)
                if materia_seleccionada:
                    encontrada = True
                    from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
                    self.main.accion = Seleccionar(self.main, materia_seleccionada)
                else:
                    self.main.interfaz_salida.mostrar_advertencia("id_no_disponible")
        else:
            self.main.interfaz_salida.mostrar_advertencia("sin_materias")

    def salir(self):
        sys.exit(0)

    def hacer_accion(self):
        self.materias = self.main.service.obtener_materias()
        
        self.main.interfaz_salida.mostrar_tabla(self.materias, self.main.service)

        opcion_elegida = self.main.interfaz_entrada.seleccionar_opcion(self.ACCIONES_DISPONIBLES)
        opcion_elegida[0]()
