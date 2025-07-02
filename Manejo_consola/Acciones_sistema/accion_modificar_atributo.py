from Manejo_consola.Acciones_sistema.accion import Accion

class Modificar_Atributo(Accion):
    def __init__(self, main, materia, atributo):
        super().__init__(main)
        self.materia_seleccionada = materia
        self.atributo = atributo
        self.TIPOS = {
            "int": self.entero,
            "float": self.decimal,
            "str": self.cadena,
            "bool": self.booleano
        }

    def cambiar_a_seleccionar(self):
        from Manejo_consola.Acciones_sistema.accion_seleccionar import Seleccionar
        self.main.accion = Seleccionar(self.main, self.materia_seleccionada)

    def entero(self):
        return self.main.interfaz_entrada.obtener_entero(self.atributo[1])
    
    def decimal(self):
        return self.main.interfaz_entrada.obtener_decimal(self.atributo[1])
    
    def cadena(self):
        return self.main.interfaz_entrada.obtener_cadena(self.atributo[1])
    
    def booleano(self):
        return self.main.interfaz_entrada.obtener_booleano(self.atributo[1])

    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.get_id_materia() == id_materia:
                return materia
        return None

    def modificar_atributo(self):
        id_actual = self.materia_seleccionada.get_id_materia()
        unica = False
        while not unica:
            valor = self.TIPOS[self.atributo[2]]()
            if self.atributo[0] == "id_materia":
                materias = self.main.service.obtener_materias()
                if not self.buscar_materia(valor, materias):
                    self.materia_seleccionada.set_id_materia(valor)
                    self.main.service.mover_notas(id_actual, valor)
                    unica = True
                else:
                    self.main.interfaz_salida.mostrar_advertencia("id_no_disponible")
            else:
                unica = True
        self.main.service.modificar_materia(id_actual, self.atributo[0], valor)

    def hacer_accion(self):
        self.modificar_atributo()
        self.cambiar_a_seleccionar()