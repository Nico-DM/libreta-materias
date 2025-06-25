from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Algun_Final_Aprobado import Algun_Final_Aprobado
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Cantidad_Finales_Menor_Max import Cantidad_Finales_Menor_Max
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Faltan_Notas_Parcial_o_Recuperatorio import Faltan_Notas_Parcial_o_Recuperatorio
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Materia_Es_Promocionable import Materia_Es_Promocionable
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Todos_Parciales_Mayor_o_Igual_Promocion import Todos_Parciales_Mayor_o_Igual_Promocion
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Todos_Parciales_o_Recuperatorio_Aprobados import Todos_Parciales_o_Recuperatorio_Aprobados
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado

class Builder_Determinador():
    def __init__(self):
        self.reset()
    
    def __cursando(self):
        self.__lista_cursando = [Faltan_Notas_Parcial_o_Recuperatorio()]

    def __promociono(self):
        self.__lista_promociono = [Materia_Es_Promocionable(), Todos_Parciales_Mayor_o_Igual_Promocion()]

    def __aprobo(self):
        self.__lista_aprobo = [Algun_Final_Aprobado()]

    def __regularizo(self):
        self.__lista_regularizo = [Todos_Parciales_o_Recuperatorio_Aprobados(), Cantidad_Finales_Menor_Max()]

    def __build(self):
        self.__resultado = Determinador_Estado(self.__lista_cursando, self.__lista_promociono, self.__lista_aprobo, self.__lista_regularizo)
    
    def reset(self):
        self.__resultado = None
        self.__lista_cursando = []
        self.__lista_promociono = []
        self.__lista_aprobo = []
        self.__lista_regularizo = []

    def construir(self):
        self.__cursando()
        self.__promociono()
        self.__aprobo()
        self.__regularizo()
        self.__build()
    
    def get_resultado(self):
        return self.__resultado