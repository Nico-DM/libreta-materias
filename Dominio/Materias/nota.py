class Nota():
    def __init__(self, datos: dict):
        try:
            self.__id_nota = int(datos["id_nota"])
        except Exception:
            self.__id_nota = None
        self.__id_materia = int(datos["id_materia"])
        self.__valor_nota = float(datos["valor_nota"])

    def get_id_nota(self):
        return self.__id_nota

    def set_id_nota(self, id):
        self.__id_nota = id
    
    def get_id_materia(self):
        return self.__id_materia

    def set_id_materia(self, id):
        self.__id_materia = id

    def get_valor_nota(self):
        return self.__valor_nota

    def set_valor_nota(self, valor):
        self.__valor_nota = valor