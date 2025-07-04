import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Todos_Parciales_Mayor_o_Igual_Promocion import Todos_Parciales_Mayor_o_Igual_Promocion
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial

class TestTodosParcialesMayorOIgualPromocion(unittest.TestCase):
    def setUp(self):
        self.evaluador = Todos_Parciales_Mayor_o_Igual_Promocion()
        self.materia = MagicMock(spec=Materia)
        self.materia.get_nota_min_promocion.return_value = 8.0

    # --- Casos normales ---
    def test_todos_parciales_mayores_o_iguales_promocion(self):
        parciales = []
        for nota in [8.0, 9.0, 10.0]:
            p = MagicMock(spec=Parcial)
            p.get_valor_nota.return_value = nota
            parciales.append(p)

        datos = Datos(self.materia, parciales, [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_todos_parciales_justo_en_el_limite(self):
        parciales = [MagicMock(spec=Parcial) for _ in range(2)]
        for p in parciales:
            p.get_valor_nota.return_value = 8.0

        datos = Datos(self.materia, parciales, [])
        self.assertTrue(self.evaluador.evaluar(datos))

    # --- Casos de error lógico ---
    def test_un_parcial_menor_a_promocion(self):
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 8.0
        p2 = MagicMock(spec=Parcial)
        p2.get_valor_nota.return_value = 6.0

        datos = Datos(self.materia, [p1, p2], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_sin_parciales(self):
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))  # Por diseño requiere al menos uno

    # --- Casos límite ---
    def test_nota_min_promocion_es_none(self):
        self.materia.get_nota_min_promocion.return_value = None
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 0.1  # cualquier nota > 0 debería dar True

        datos = Datos(self.materia, [p1], [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_nota_igual_a_cero_y_criterio_es_none(self):
        self.materia.get_nota_min_promocion.return_value = None
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 0.0  # justo igual al criterio asumido (0)

        datos = Datos(self.materia, [p1], [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_nota_menor_a_cero_con_criterio_none(self):
        self.materia.get_nota_min_promocion.return_value = None
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = -1.0

        datos = Datos(self.materia, [p1], [])
        self.assertFalse(self.evaluador.evaluar(datos))

if __name__ == '__main__':
    unittest.main()
