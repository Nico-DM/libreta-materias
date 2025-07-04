import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Cantidad_Finales_Menor_Max import Cantidad_Finales_Menor_Max
from Dominio.Materias.materia import Materia
from Dominio.Materias.final import Final

class TestCantidadFinalesMenorMax(unittest.TestCase):
    def setUp(self):
        self.evaluador = Cantidad_Finales_Menor_Max()
        self.materia = MagicMock(spec=Materia)

    # --- Casos normales ---
    def test_menos_finales_que_maximo(self):
        self.materia.get_cant_veces_final_rendible.return_value = 3
        finales = [MagicMock(spec=Final) for _ in range(2)]  # 2 intentos

        datos = Datos(self.materia, [], finales)
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_sin_finales_y_limite_positivo(self):
        self.materia.get_cant_veces_final_rendible.return_value = 3
        datos = Datos(self.materia, [], [])  # 0 intentos
        self.assertTrue(self.evaluador.evaluar(datos))

    # --- Casos de error lógico (límite alcanzado o superado) ---
    def test_igual_cantidad_finales_que_maximo(self):
        self.materia.get_cant_veces_final_rendible.return_value = 2
        finales = [MagicMock(spec=Final) for _ in range(2)]  # justo el máximo

        datos = Datos(self.materia, [], finales)
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_mas_finales_que_maximo(self):
        self.materia.get_cant_veces_final_rendible.return_value = 1
        finales = [MagicMock(spec=Final) for _ in range(3)]

        datos = Datos(self.materia, [], finales)
        self.assertFalse(self.evaluador.evaluar(datos))

    # --- Casos límite ---
    def test_maximo_cero_con_finales(self):
        self.materia.get_cant_veces_final_rendible.return_value = 0
        finales = [MagicMock(spec=Final) for _ in range(1)]  # ya se pasó

        datos = Datos(self.materia, [], finales)
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_maximo_cero_sin_finales(self):
        self.materia.get_cant_veces_final_rendible.return_value = 0
        datos = Datos(self.materia, [], [])  # 0/0

        self.assertFalse(self.evaluador.evaluar(datos))

if __name__ == '__main__':
    unittest.main()
