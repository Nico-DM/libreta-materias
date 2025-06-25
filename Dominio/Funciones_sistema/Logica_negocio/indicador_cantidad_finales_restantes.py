from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Cantidad_Finales_Menor_Max import Cantidad_Finales_Menor_Max

class Indicador_Cantidad_Finales_Restantes():
    def __init__(self, calculador: Cantidad_Finales_Menor_Max):
        self.calculador: Cantidad_Finales_Menor_Max = calculador

    def cantidad_finales_restante(self, finales, materia):
        return self.calculador.calcular_intentos_restantes(finales, materia.get_cant_veces_final_rendible())