class Materia():
    def __init__(self, datos: dict):
        self.__id_materia = int(datos["id_materia"])
        self.__nombre_materia = str(datos["nombre_materia"])
        self.__nombre_docente = str(datos["nombre_docente"])
        self.__nota_min_aprobar = float(datos["nota_min_aprobar"])
        self.__es_promocionable = datos["es_promocionable"]
        try:
            self.__nota_min_promocion = float(datos["nota_min_promocion"])
        except Exception:
            self.__nota_min_promocion = None
        self.__cant_veces_final_rendible = int(datos["cant_veces_final_rendible"])
        self.__cant_parciales = int(datos["cant_parciales"])

    def get_id_materia(self):
        return self.__id_materia

    def set_id_materia(self, id):
        self.__id_materia = id
    
    def get_nombre_materia(self):
        return self.__nombre_materia

    def set_nombre_materia(self, nombre):
        self.__nombre_materia = nombre

    def get_nombre_docente(self):
        return self.__nombre_docente
    
    def set_nombre_docente(self, nombre):
        self.__nombre_docente = nombre

    def get_nota_min_aprobar(self):
        return self.__nota_min_aprobar
    
    def set_nota_min_aprobar(self, nota_minima):
        self.__nota_min_aprobar = nota_minima

    def get_es_promocionable(self):
        return self.__es_promocionable
    
    def set_es_promocionable(self, es_promocionable):
        self.__es_promocionable = es_promocionable

    def get_nota_min_promocion(self):
        return self.__nota_min_promocion
    
    def set_nota_min_promocion(self, nota_minima):
        self.__nota_min_promocion = nota_minima

    def get_cant_veces_final_rendible(self):
        return self.__cant_veces_final_rendible
    
    def set_cant_veces_final_rendible(self, cant):
        self.__cant_veces_final_rendible = cant

    def get_cant_parciales(self):
        return self.__cant_parciales
    
    def set_cant_parciales(self, cantidad):
        self.__cant_parciales = cantidad
