import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Materia_Es_Promocionable import Materia_Es_Promocionable
from Dominio.Materias.materia import Materia

class TestMateriaEsPromocionable(unittest.TestCase):
    def setUp(self):
        self.evaluador = Materia_Es_Promocionable()
        self.materia = MagicMock(spec=Materia)

    # --- Casos normales ---
    def test_materia_es_promocionable_true(self):
        self.materia.get_es_promocionable.return_value = True
        datos = Datos(self.materia, [], [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_materia_es_promocionable_false(self):
        self.materia.get_es_promocionable.return_value = False
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    # --- Casos límite ---
    def test_materia_es_promocionable_none(self):
        self.materia.get_es_promocionable.return_value = None
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))  # Interpretamos None como no promocionable

    def test_materia_es_promocionable_string_true(self):
        self.materia.get_es_promocionable.return_value = "True"
        datos = Datos(self.materia, [], [])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_materia_es_promocionable_empty_string(self):
        self.materia.get_es_promocionable.return_value = ""
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))

if __name__ == '__main__':
    unittest.main()
