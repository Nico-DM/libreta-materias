from flask import Blueprint, request, jsonify
from api.dto import materia_to_dict, parcial_to_dict, final_to_dict, materia_con_resultados_to_dict

def crear_rutas(service):
    bp = Blueprint("materias", __name__)

    @bp.route("/materias", methods=["POST"])
    def crear():
        data = request.get_json()
        datos = data.get("datos_materia")
        materia = service.crear_materia(datos)
        return jsonify(materia_to_dict(materia)), 201

    @bp.route("/materias/<id_materia>/agregar_parcial", methods=["POST"])
    def agregar_parcial(id_materia):
        data = request.get_json()
        valor = float(data.get("valor"))

        try:
            parcial = service.agregar_parcial(int(id_materia), valor)
            return jsonify(parcial_to_dict(parcial))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    @bp.route("/materias/<id_materia>/agregar_final", methods=["POST"])
    def agregar_final(id_materia):
        data = request.get_json()
        valor = float(data.get("valor"))

        try:
            final = service.agregar_final(int(id_materia), valor)
            return jsonify(final_to_dict(final))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    @bp.route("/materias/<id_materia>/agregar_recuperatorio", methods=["POST"])
    def agregar_recuperatorio(id_materia):
        data = request.get_json()
        id_nota = int(data.get("id_nota"))
        valor = float(data.get("valor"))

        try:
            parcial = service.agregar_recuperatorio(int(id_materia), id_nota, valor)
            return jsonify(parcial_to_dict(parcial))
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @bp.route("/materias/<id_materia>", methods=["GET"])
    def obtener(id_materia):
        try:
            materia, resultados = service.obtener_materia_con_resultados(int(id_materia))
            return jsonify(materia_con_resultados_to_dict(materia, resultados))
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    @bp.route("/materias", methods=["GET"])
    def listar_materias():
        materias = service.obtener_materias()
        materias_dict = []
        for m in materias:
            materias_dict.append(materia_to_dict(m))
        return jsonify(materias_dict)

    @bp.route("/materias/<int:id_materia>", methods=["DELETE"])
    def eliminar_materia(id_materia):
        service.eliminar_materia(id_materia)
        return jsonify({"mensaje": "Materia eliminada correctamente"}), 200

    @bp.route("/materias/<int:id_materia>", methods=["PUT"])
    def modificar_materia(id_materia):
        data = request.get_json()
        atributo = data.get("atributo")
        valor = data.get("valor")
        service.modificar_materia(id_materia, atributo, valor)
        return jsonify({"mensaje": "Materia modificada correctamente"}), 200

    @bp.route("/materias/<int:id_materia>/parciales", methods=["GET"])
    def obtener_parciales(id_materia):
        parciales = service.obtener_parciales(int(id_materia))
        parciales_dict = []
        for p in parciales:
            parciales_dict.append(parcial_to_dict(p))
        return jsonify(parciales_dict)

    @bp.route("/parciales/<int:id_parcial>", methods=["PUT"])
    def modificar_parcial(id_parcial):
        data = request.get_json()
        atributo = data.get("atributo")
        valor = data.get("valor")
        service.modificar_parcial(id_parcial, atributo, valor)
        return jsonify({"mensaje": "Parcial modificado correctamente"}), 200
    
    @bp.route("/materias/<int:id_materia>/finales", methods=["GET"])
    def obtener_finales(id_materia):
        finales = service.obtener_finales(int(id_materia))
        finales_dict = []
        for f in finales:
            finales_dict.append(final_to_dict(f))
        return jsonify(finales_dict)

    @bp.route("/finales/<int:id_final>", methods=["PUT"])
    def modificar_final(id_final):
        data = request.get_json()
        atributo = data.get("atributo")
        valor = data.get("valor")
        service.modificar_final(id_final, atributo, valor)
        return jsonify({"mensaje": "Final modificado correctamente"}), 200

    @bp.route("/materias/eliminar_base", methods=["DELETE"])
    def eliminar_base():
        service.eliminar_base()
        return jsonify({"mensaje": "Base eliminada correctamente"}), 200

    @bp.route("/materias/mover_notas", methods=["PUT"])
    def mover_notas():
        data = request.get_json()
        id_vieja = int(data.get("id_vieja"))
        id_nueva = int(data.get("id_nueva"))
        service.mover_notas(id_vieja, id_nueva)
        return jsonify({"mensaje": "Notas movidas correctamente"}), 200

    return bp