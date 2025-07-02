from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Manejo_consola.cli import CLI
from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
from api.materia_service import MateriaService
from api.handlers import MateriaHandler, ParcialHandler, FinalHandler

class Main():
    def __init__(self):
        self.interfaz_entrada = CLI()
        self.interfaz_salida = self.interfaz_entrada
        self.accion = Mostrar_Tabla(self)

        repo = Facade_Persistencia()
        repo.crear_base()
        builder = Builder_Determinador()
        builder.construir()
        determiner = builder.get_resultado()
        builder.reset()
        handlers = {
            "materia": MateriaHandler(repo),
            "parcial": ParcialHandler(repo),
            "final": FinalHandler(repo)
        }

        self.service = MateriaService(determiner, handlers)

    def main(self):
        while True:
            self.accion.hacer_accion()

if __name__ == "__main__":
    main_ = Main()
    main_.main()