from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado

class MateriaService:
    def __init__(self, estado_determiner, handlers, promediador, indicador_cantidad_finales):
        self.determiner = estado_determiner
        self.handlers = handlers
        self.promediador = promediador
        self.indicador_cantidad_finales = indicador_cantidad_finales

    def crear_materia(self, datos: dict):
        materia = Materia(datos)
        self.handlers["materia"].agregar(materia)
        return materia
    
    def obtener_materias(self):
        return self.handlers["materia"].obtener_todas()
    
    def eliminar_materia(self, id: int):
        self.handlers["materia"].eliminar(id)
    
    def modificar_materia(self, id: int, atributo: str, valor):
        self.handlers["materia"].modificar(id, atributo, valor)

    def agregar_parcial(self, id: int, valor: float):
        parcial = Parcial({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
                "valor_recuperatorio": None
            })

        self.handlers["parcial"].agregar(parcial)
        return parcial
    
    def modificar_parcial(self, id: int, atributo: str, valor):
        self.handlers["parcial"].modificar(id, atributo, valor)
    
    def obtener_parciales(self, id_materia):
        materia = self.handlers["materia"].obtener(id_materia)
        return self.handlers["parcial"].obtener_todas_de(materia)
    
    def agregar_final(self, id: int, valor: float):
        final = Final({
                "id_nota": None,
                "id_materia": id,
                "valor_nota": valor,
            })

        self.handlers["final"].agregar(final)
        return final
    
    def modificar_final(self, id: int, atributo: str, valor):
        self.handlers["final"].modificar(id, atributo, valor)
    
    def obtener_finales(self, id_materia):
        materia = self.handlers["materia"].obtener(id_materia)
        return self.handlers["final"].obtener_todas_de(materia)

    def agregar_recuperatorio(self, id_materia: int, id_nota: int, valor: float):
        self.handlers["parcial"].agregar_recuperatorio(id_materia, id_nota, valor)
        parcial = self.handlers["parcial"].obtener(id_nota)
        return parcial
    
    def determinar_resultados(self, materia):
        id_materia = materia.get_id_materia()
        parciales = self.obtener_parciales(id_materia)
        finales = self.obtener_finales(id_materia)
        resultados = {}
        estado = self.determiner.determinar_estado(Datos(materia, parciales, finales))
        resultados["estado"] = estado
        if estado == Estado.APROBADO:
            resultados["nota_final"] = finales[-1].get_valor_nota()
        elif estado == Estado.PROMOCIONADO:
            resultados["nota_final"] = self.promediador.promediar(parciales)
        elif estado == Estado.REGULARIZADO:
            resultados["intentos_final_restantes"] = self.indicador_cantidad_finales.cantidad_finales_restante(finales, materia)
        return resultados

    def obtener_materia_con_resultados(self, id: int):
        try:
            materia = self.handlers["materia"].obtener(id)
            resultados = self.determinar_resultados(materia)
            return materia, resultados
        except Exception:
            raise ValueError("Materia no encontrada")
    
    def eliminar_base(self):
        self.handlers["repo"].eliminar_base()
    
    def mover_notas(self, id_vieja: int, id_nueva: int):
        self.handlers["repo"].mover_notas(id_vieja, id_nueva)