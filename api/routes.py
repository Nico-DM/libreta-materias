from flask import Blueprint, request, jsonify
from api.dto import materia_to_dict, parcial_to_dict, final_to_dict, materia_con_estado_to_dict

def crear_rutas(controller):
    bp = Blueprint("materias", __name__)

    @bp.route("/materias", methods=["POST"])
    def crear():
        data = request.get_json()
        datos = data.get("datos_materia")
        materia = controller.crear_materia(datos)
        return jsonify(materia_to_dict(materia)), 201

    @bp.route("/materias/<id_materia>/agregar_parcial", methods=["POST"])
    def agregar_parcial(id_materia):
        data = request.get_json()
        valor = float(data.get("valor"))

        try:
            parcial = controller.agregar_parcial(int(id_materia), valor)
            return jsonify(parcial_to_dict(parcial))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    @bp.route("/materias/<id_materia>/agregar_final", methods=["POST"])
    def agregar_final(id_materia):
        data = request.get_json()
        valor = float(data.get("valor"))

        try:
            final = controller.agregar_final(int(id_materia), valor)
            return jsonify(final_to_dict(final))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    @bp.route("/materias/<id_materia>/agregar_recuperatorio", methods=["POST"])
    def agregar_recuperatorio(id_materia):
        data = request.get_json()
        id_nota = int(data.get("id_nota"))
        valor = float(data.get("valor"))

        try:
            parcial = controller.agregar_recuperatorio(int(id_materia), id_nota, valor)
            return jsonify(parcial_to_dict(parcial))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @bp.route("/materias/<id_materia>", methods=["GET"])
    def obtener(id_materia):
        try:
            materia, estado = controller.obtener_materia_con_estado(int(id_materia))
            return jsonify(materia_con_estado_to_dict(materia, estado))
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    return bp