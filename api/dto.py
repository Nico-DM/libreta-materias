from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final

def materia_to_dict(materia: Materia):
    return {
        "id_materia": materia.get_id_materia(),
        "nombre_materia": materia.get_nombre_materia(),
        "nombre_docente": materia.get_nombre_docente(),
        "nota_min_aprobar": materia.get_nota_min_aprobar(),
        "es_promocionable": materia.get_es_promocionable(),
        "nota_min_promocion": materia.get_nota_min_promocion(),
        "cant_veces_final_rendible": materia.get_cant_veces_final_rendible(),
        "cant_parciales": materia.get_cant_parciales()
    }

def parcial_to_dict(parcial: Parcial):
    return {
            "id_nota": parcial.get_id_nota(),
            "id_materia": parcial.get_id_materia(),
            "valor_nota": parcial.get_valor_nota(),
            "valor_recuperatorio": parcial.get_valor_recuperatorio()
        }

def final_to_dict(final: Final):
    return {
            "id_nota": final.get_id_nota(),
            "id_materia": final.get_id_materia(),
            "valor_nota": final.get_valor_nota()
        }

def materia_con_notas_to_dict(materia: Materia, parciales: list[Parcial], finales: list[Final]):
    parciales_dict = []
    for parcial in parciales:
        parciales_dict.append(parcial_to_dict(parcial))
    
    finales_dict = []
    for final in finales:
        finales_dict.append(final_to_dict(final))
    
    return {
        "datos_materia": materia_to_dict(materia),
        "parciales": parciales_dict,
        "finales": finales_dict
    }

def resultados_to_dict(resultados):
    diccionario = {}
    diccionario["estado"] = resultados["estado"].name
    try:
        diccionario["nota_final"] = resultados["nota_final"]
    except KeyError:
        diccionario["nota_final"] = None
    try:
        diccionario["intentos_final_restantes"] = resultados["intentos_final_restantes"]
    except KeyError:
        diccionario["intentos_final_restantes"] = None
    return diccionario

def materia_con_resultados_to_dict(materia, resultados):
    return {
        "datos_materia": materia_to_dict(materia),
        "resultados": resultados_to_dict(resultados)
    }