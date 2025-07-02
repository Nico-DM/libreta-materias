from Manejo_consola.Acciones_sistema.accion import Accion
from Dominio.Materias.materia import Materia

class Agregar(Accion):
    def __init__(self, main):
        super().__init__(main)
        self.ATRIBUTOS = [
            ("id_materia", "ID de la Materia", "int"),
            ("nombre_materia", "Nombre de la Materia", "str"),
            ("nombre_docente", "Nombre de el/la Docente", "str"),
            ("nota_min_aprobar", "Nota mínima para Aprobar un parcial/final", "float"),
            ("es_promocionable", "¿Es promocionable?", "bool"),
            ("nota_min_promocion", "Nota mínima para Promocionar (si aplica)", "float"),
            ("cant_veces_final_rendible", "Cantidad de oportunidades para rendir el final", "int"),
            ("cant_parciales", "Cantidad de parciales de la materia", "int")
        ]
        self.TIPOS = {
            "int": self.entero,
            "float": self.decimal,
            "str": self.cadena,
            "bool": self.booleano
        }
    
    def entero(self, atributo):
        return self.main.interfaz_entrada.obtener_entero(atributo[1])
    
    def decimal(self, atributo):
        return self.main.interfaz_entrada.obtener_decimal(atributo[1])
    
    def cadena(self, atributo):
        return self.main.interfaz_entrada.obtener_cadena(atributo[1])
    
    def booleano(self, atributo):
        return self.main.interfaz_entrada.obtener_booleano(atributo[1])

    def cambiar_a_mostrar(self):
        from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
        self.main.accion = Mostrar_Tabla(self.main)

    def buscar_materia(self, id_materia, materias):
        for materia in materias:
            if materia.get_id_materia() == id_materia:
                return materia
        return None

    def hacer_accion(self):
        datos = {}

        materias = self.main.service.obtener_materias()
        unica = False
        while not unica:
            dato = self.TIPOS[self.ATRIBUTOS[0][2]](self.ATRIBUTOS[0])
            if not self.buscar_materia(dato, materias):
                unica = True
            else:
                self.main.interfaz_salida.mostrar_advertencia("id_no_disponible")

        datos[self.ATRIBUTOS[0]] = dato

        for i in range(1, len(self.ATRIBUTOS)):
            dato = self.TIPOS[self.ATRIBUTOS[i][2]](self.ATRIBUTOS[i])
            datos[self.ATRIBUTOS[i]] = dato

        self.main.service.crear_materia(datos)

        self.main.interfaz_salida.mostrar_advertencia("materia_agregada")

        self.cambiar_a_mostrar()