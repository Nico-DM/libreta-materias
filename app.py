from flask import Flask
from api.routes import crear_rutas
from api.controller import MateriaController
from api.nota_handlers import ParcialHandler, RecuperatorioHandler, FinalHandler

# tus clases reales del dominio
from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador

app = Flask(__name__)

repo = Facade_Persistencia()
repo.crear_base()
builder = Builder_Determinador()
builder.construir()
determiner = builder.get_resultado()
builder.reset()
handlers = {
    "parcial": ParcialHandler(),
    "recuperatorio": RecuperatorioHandler(),
    "final": FinalHandler()
}

controller = MateriaController(repo, determiner)

app.register_blueprint(crear_rutas(controller))

if __name__ == "__main__":
    app.run(debug=True)