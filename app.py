from flask import Flask
from api.routes import crear_rutas
from api.materia_service import MateriaService
from api.handlers import MateriaHandler, ParcialHandler, FinalHandler, RepoHandler

from Persistencia.Facade_Persistencia import Facade_Persistencia
from Dominio.Funciones_sistema.Logica_negocio.builder_determinador import Builder_Determinador

app = Flask(__name__)

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

service = MateriaService(determiner, handlers)

app.register_blueprint(crear_rutas(service))

if __name__ == "__main__":
    app.run(debug=True)