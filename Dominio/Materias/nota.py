class Nota():
    def __init__(self, tupla):
        try:
            self.__id_nota = int(tupla[0])
        except Exception:
            self.__id_nota = None
        self.__id_materia = int(tupla[1])
        self.__valor_nota = float(tupla[2])

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