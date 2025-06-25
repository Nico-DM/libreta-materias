# libreta-materias

Perfecto, volvamos entonces a la versión correcta y limpia de `agregar_nota` con el uso de handlers por tipo de nota, pero sin calcular el estado en ese momento (ya que el estado solo se consulta desde un endpoint dedicado).

---

✅ **Versión final corregida**

---

### `controller.py`

```python
# api/controller.py

class MateriaController:
    def __init__(self, materia_repo, estado_determiner, nota_handlers: dict):
        self.repo = materia_repo
        self.determiner = estado_determiner  # solo usado para consulta
        self.handlers = nota_handlers        # dict con handlers por tipo de nota

    def crear_materia(self, nombre: str):
        materia = Materia(nombre)
        self.repo.guardar(materia)
        return materia

    def agregar_nota(self, nombre: str, tipo: str, nota: float):
        if tipo not in self.handlers:
            raise ValueError(f"Tipo de nota no soportado: {tipo}")

        materia = self.repo.obtener(nombre)
        if not materia:
            raise ValueError("Materia no encontrada")

        self.handlers[tipo].ejecutar(materia, nota)
        self.repo.guardar(materia)
        return materia

    def obtener_materia_con_estado(self, nombre: str):
        materia = self.repo.obtener(nombre)
        if not materia:
            raise ValueError("Materia no encontrada")
        estado = self.determiner.determinar_estado(materia)
        return materia, estado
```

---

### `nota_handlers.py` (igual que antes)

```python
# api/nota_handlers.py
from abc import ABC, abstractmethod

class NotaHandler(ABC):
    @abstractmethod
    def ejecutar(self, materia, nota): pass

class ParcialHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_parcial(nota)

class RecuperatorioHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_recuperatorio(nota)

class FinalHandler(NotaHandler):
    def ejecutar(self, materia, nota):
        materia.agregar_final(nota)
```

---

### `dto.py`

```python
# api/dto.py
def materia_to_dict(materia):
    return {
        "nombre": materia.nombre,
        "parciales": materia.parciales,
        "recuperatorios": materia.recuperatorios,
        "finales": materia.finales,
    }

def materia_con_estado_to_dict(materia, estado):
    return {
        **materia_to_dict(materia),
        "estado": estado
    }
```

---

### `routes.py`

```python
# api/routes.py
from flask import Blueprint, request, jsonify
from api.dto import materia_to_dict, materia_con_estado_to_dict

def crear_rutas(controller):
    bp = Blueprint("materias", __name__)

    @bp.route("/materias", methods=["POST"])
    def crear():
        data = request.get_json()
        nombre = data.get("nombre")
        materia = controller.crear_materia(nombre)
        return jsonify(materia_to_dict(materia)), 201

    @bp.route("/materias/<nombre>/notas", methods=["POST"])
    def agregar_nota(nombre):
        data = request.get_json()
        tipo = data.get("tipo")  # "parcial", "recuperatorio" o "final"
        nota = data.get("nota")

        try:
            materia = controller.agregar_nota(nombre, tipo, nota)
            return jsonify(materia_to_dict(materia))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @bp.route("/materias/<nombre>", methods=["GET"])
    def obtener(nombre):
        try:
            materia, estado = controller.obtener_materia_con_estado(nombre)
            return jsonify(materia_con_estado_to_dict(materia, estado))
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    return bp
```

---

### `app.py`

```python
# app.py
from flask import Flask
from api.routes import crear_rutas
from api.controller import MateriaController
from api.nota_handlers import ParcialHandler, RecuperatorioHandler, FinalHandler

# tus clases reales del dominio
from dominio.repositorio import RepositorioMateria
from dominio.determinador import DeterminadorDeEstados

app = Flask(__name__)

repo = RepositorioMateria()
determiner = DeterminadorDeEstados()
handlers = {
    "parcial": ParcialHandler(),
    "recuperatorio": RecuperatorioHandler(),
    "final": FinalHandler()
}

controller = MateriaController(repo, determiner, handlers)

app.register_blueprint(crear_rutas(controller))

if __name__ == "__main__":
    app.run(debug=True)
```

---

✅ **Resultado**

- ✔️ Notas se agregan desacopladas y extensibles vía handlers.
- ✔️ El estado no se calcula ni guarda al modificar la materia.
- ✔️ Solo se calcula al hacer un `GET /materias/<nombre>`.
- ✔️ Se mantiene SOLID y una arquitectura limpia.

---

## 🧪 Ejemplos para probar la API

Suponiendo que corre en `http://localhost:5000`:

### ✅ 1. Crear una materia

**Request:** `POST /materias`  
**Body:**
```json
{
  "nombre": "Análisis Matemático"
}
```
**cURL:**
```bash
curl -X POST http://localhost:5000/materias   -H "Content-Type: application/json"   -d '{"nombre": "Análisis Matemático"}'
```

---

### ✅ 2. Agregar una nota (ej: parcial)

**Request:** `POST /materias/Análisis Matemático/notas`  
**Body:**
```json
{
  "tipo": "parcial",
  "nota": 9
}
```
**cURL:**
```bash
curl -X POST "http://localhost:5000/materias/Análisis Matemático/notas"   -H "Content-Type: application/json"   -d '{"tipo": "parcial", "nota": 9}'
```

> Podés cambiar `"tipo"` a `"recuperatorio"` o `"final"` según corresponda.

---

### ✅ 3. Consultar estado de la materia

**Request:** `GET /materias/Análisis Matemático`  
**cURL:**
```bash
curl http://localhost:5000/materias/Análisis%20Matemático
```

**Respuesta esperada:**
```json
{
  "nombre": "Análisis Matemático",
  "parciales": [9],
  "recuperatorios": [],
  "finales": [],
  "estado": "Cursando"  // O el que determine tu lógica
}
```