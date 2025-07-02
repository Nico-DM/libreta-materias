from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, repo):
        super().__init__()
        self.repo = repo
    
    @abstractmethod
    def agregar(self, objeto): pass

    @abstractmethod
    def obtener(self, id): pass

    @abstractmethod
    def modificar(self, id, atributo, valor): pass

class MateriaHandler(Handler):
    def agregar(self, objeto):
        self.repo.agregar_materia(objeto)
    
    def obtener(self, id):
        return self.repo.obtener_materia(id)
    
    def obtener_todas(self):
        return self.repo.obtener_materias()
    
    def eliminar(self, id):
        self.repo.eliminar_materia(id)
    
    def modificar(self, id, atributo, valor):
        self.repo.modificar_materia(id, atributo, valor)

class NotaHandler(Handler):
    @abstractmethod
    def obtener_todas_de(self, materia): pass

class ParcialHandler(NotaHandler):
    def agregar(self, objeto):
        self.repo.agregar_parcial(objeto)
    
    def obtener(self, id):
        return self.repo.obtener_parcial(id)
    
    def obtener_todas_de(self, materia):
        return self.repo.obtener_parciales(materia)
    
    def agregar_recuperatorio(self, id_materia, id_nota, valor):
        self.repo.agregar_recuperatorio(id_materia, id_nota, valor)
    
    def modificar(self, id, atributo, valor):
        self.repo.modificar_parcial(id, atributo, valor)

class FinalHandler(NotaHandler):
    def agregar(self, objeto):
        self.repo.agregar_final(objeto)
    
    def obtener(self, id):
        return self.repo.obtener_final(id)
    
    def obtener_todas_de(self, materia):
        return self.repo.obtener_finales(materia)
    
    def modificar(self, id, atributo, valor):
        self.repo.modificar_final(id, atributo, valor)

class RepoHandler():
    def __init__(self, repo):
        self.repo = repo

    def eliminar_base(self):
        self.repo.eliminar_base()
    
    def mover_notas(self, id_vieja, id_nueva):
        self.repo.mover_notas(id_vieja, id_nueva)