import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Todos_Parciales_o_Recuperatorio_Aprobados import Todos_Parciales_o_Recuperatorio_Aprobados
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial

class TestTodosParcialesORecuperatorioAprobados(unittest.TestCase):
    def setUp(self):
        self.evaluador = Todos_Parciales_o_Recuperatorio_Aprobados()
        self.materia = MagicMock(spec=Materia)
        self.materia.get_nota_min_aprobar.return_value = 6.0

    # --- Casos normales ---
    def test_todos_aprobados_sin_recuperatorio(self):
        parciales = []
        for nota in [6.0, 7.0, 9.0]:
            p = MagicMock(spec=Parcial)
            p.get_valor_nota.return_value = nota
            p.get_valor_recuperatorio.return_value = None
            parciales.append(p)

        datos = Datos(self.materia, parciales, [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_desaprobado_con_recuperatorio_aprobado(self):
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 5.0
        p1.get_valor_recuperatorio.return_value = 6.5

        p2 = MagicMock(spec=Parcial)
        p2.get_valor_nota.return_value = 8.0
        p2.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [p1, p2], [])
        self.assertTrue(self.evaluador.evaluar(datos))

    # --- Casos de error lógico ---
    def test_desaprobado_sin_recuperatorio(self):
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 5.0
        p1.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [p1], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_desaprobado_con_recuperatorio_menor(self):
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 3.0
        p1.get_valor_recuperatorio.return_value = 5.5

        datos = Datos(self.materia, [p1], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    # --- Casos límite ---
    def test_sin_parciales(self):
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))  # requiere al menos un parcial

    def test_todos_justo_en_el_limite(self):
        parciales = [MagicMock(spec=Parcial) for _ in range(3)]
        for p in parciales:
            p.get_valor_nota.return_value = 6.0
            p.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, parciales, [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_desaprobado_y_recuperatorio_es_none(self):
        p1 = MagicMock(spec=Parcial)
        p1.get_valor_nota.return_value = 4.0
        p1.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [p1], [])
        self.assertFalse(self.evaluador.evaluar(datos))

if __name__ == '__main__':
    unittest.main()
