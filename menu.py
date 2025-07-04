from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador
from Dominio.Funciones_sistema.Calculos_notas.promedio import Promedio
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Cantidad_Finales_Menor_Max import Cantidad_Finales_Menor_Max
from Dominio.Funciones_sistema.Logica_negocio.indicador_cantidad_finales_restantes import Indicador_Cantidad_Finales_Restantes
from Manejo_consola.cli import CLI
from Manejo_consola.Acciones_sistema.accion_mostrar_tabla import Mostrar_Tabla
from api.materia_service import MateriaService
from api.handlers import MateriaHandler, ParcialHandler, FinalHandler, RepoHandler

class Menu():
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
            "final": FinalHandler(repo),
            "repo": RepoHandler(repo)
        }
        promediador = Promedio()
        indicador_cantidad_finales = Indicador_Cantidad_Finales_Restantes(Cantidad_Finales_Menor_Max())

        self.service = MateriaService(determiner, handlers, promediador, indicador_cantidad_finales)

    def menu(self):
        while True:
            self.accion.hacer_accion()

if __name__ == "__main__":
    menu = Menu()
    menu.menu()