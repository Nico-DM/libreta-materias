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