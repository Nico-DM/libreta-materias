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