from Manejo_consola.Acciones_sistema.accion import Accion

class Modificar(Accion):
    def __init__(self, menu, materia):
        super().__init__(menu)
        self.materia_seleccionada = materia
        self.OPCIONES_DISPONIBLES = {
            "A": (self.elegir_atributo, "Modificar atributo"),
            "P": (self.modificar_parcial, "Modificar parcial"),
            "F": (self.modificar_final, "Modificar final"),
            "X": (self.volver, "Volver")
        }
        self.ATRIBUTOS_DISPONIBLES = {
            "I": ("id_materia", "ID de la Materia", "int"),
            "N": ("nombre_materia", "Nombre de la Materia", "str"),
            "D": ("nombre_docente", "Nombre de el/la Docente", "str"),
            "A": ("nota_min_aprobar", "Nota mínima para Aprobar un parcial/final", "float"),
            "E": ("es_promocionable", "¿Es promocionable?", "bool"),
            "P": ("nota_min_promocion", "Nota mínima para Promocionar (si aplica)", "float"),
            "F": ("cant_veces_final_rendible", "Cantidad de oportunidades para rendir el final", "int"),
            "C": ("cant_parciales", "Cantidad de parciales de la materia", "int")
        }

    def elegir_atributo(self):
        atributo_elegido = self.menu.interfaz_entrada.seleccionar_opcion(self.ATRIBUTOS_DISPONIBLES)
        self.cambiar_a_modificar_atributo(atributo_elegido)

    def buscar_nota(self, id_nota, notas):
        for nota in notas:
            if nota.get_id_nota() == id_nota:
                return nota
        return None

    def modificar_parcial(self):
        notas = self.menu.service.obtener_parciales(self.materia_seleccionada)

        if len(notas) > 0:
            self.menu.interfaz_salida.mostrar_notas(notas, recu=True, id=True)

            encontrada = False
            while not encontrada:
                id_elegida = self.menu.interfaz_entrada.obtener_entero("ID")
                nota_seleccionada = self.buscar_nota(id_elegida, notas)
                if nota_seleccionada:
                    encontrada = True
                else:
                    self.menu.interfaz_salida.mostrar_advertencia("id_no_disponible")

            from Manejo_consola.Acciones_sistema.accion_modificar_parcial import Modificar_Parcial
            self.menu.accion = Modificar_Parcial(self.menu, self.materia_seleccionada, id_elegida)
        else:
            self.menu.interfaz_salida.mostrar_advertencia("sin_notas")
            self.volver()
    
    def modificar_final(self):
        notas = self.menu.service.obtener_finales(self.materia_seleccionada)

        if len(notas) > 0:
            self.menu.interfaz_salida.mostrar_notas(notas, id=True)

            encontrada = False
            while not encontrada:
                id_elegida = self.menu.interfaz_entrada.obtener_entero("ID")
                nota_seleccionada = self.buscar_nota(id_elegida, notas)
                if nota_seleccionada:
                    encontrada = True
                else:
                    self.menu.interfaz_salida.mostrar_advertencia("id_inexistente")

            from Manejo_consola.Acciones_sistema.accion_modificar_final import Modificar_Final
            self.menu.accion = Modificar_Final(self.menu, self.materia_seleccionada, id_elegida)
        else:
            self.menu.interfaz_salida.mostrar_advertencia("sin_notas")
            self.volver()

    def cambiar_a_modificar_atributo(self, atributo):
        from Manejo_consola.Acciones_sistema.accion_modificar_atributo import Modificar_Atributo
        self.menu.accion = Modificar_Atributo(self.menu, self.materia_seleccionada, atributo)

    def volver(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.menu.accion = Seleccionar(self.menu, self.materia_seleccionada)

    def hacer_accion(self):
        opcion_elegida = self.menu.interfaz_entrada.seleccionar_opcion(self.OPCIONES_DISPONIBLES)
        opcion_elegida[0]()
