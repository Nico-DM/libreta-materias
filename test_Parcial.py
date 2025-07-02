import unittest
from Dominio.Materias.parcial import Parcial

class TestParcial(unittest.TestCase):

    def test_constructor_completo_valido(self):
        datos = {
            "id_nota": "1",
            "id_materia": "101",
            "valor_nota": "8.0",
            "valor_recuperatorio": "7.5"
        }
        parcial = Parcial(datos)
        self.assertEqual(parcial.get_id_nota(), 1)
        self.assertEqual(parcial.get_id_materia(), 101)
        self.assertEqual(parcial.get_valor_nota(), 8.0)
        self.assertEqual(parcial.get_valor_recuperatorio(), 7.5)

    def test_constructor_sin_valor_recuperatorio(self):
        datos = {
            "id_nota": "2",
            "id_materia": "102",
            "valor_nota": "5.0"
            # sin "valor_recuperatorio"
        }
        parcial = Parcial(datos)
        self.assertEqual(parcial.get_id_nota(), 2)
        self.assertEqual(parcial.get_id_materia(), 102)
        self.assertEqual(parcial.get_valor_nota(), 5.0)
        self.assertIsNone(parcial.get_valor_recuperatorio())

    def test_constructor_valor_recuperatorio_invalido(self):
        datos = {
            "id_nota": "3",
            "id_materia": "103",
            "valor_nota": "6.0",
            "valor_recuperatorio": "abc"
        }
        parcial = Parcial(datos)
        self.assertEqual(parcial.get_id_nota(), 3)
        self.assertEqual(parcial.get_id_materia(), 103)
        self.assertEqual(parcial.get_valor_nota(), 6.0)
        self.assertIsNone(parcial.get_valor_recuperatorio())

    def test_set_get_valor_recuperatorio(self):
        datos = {
            "id_nota": "4",
            "id_materia": "104",
            "valor_nota": "4.0"
        }
        parcial = Parcial(datos)
        parcial.set_valor_recuperatorio(6.5)
        self.assertEqual(parcial.get_valor_recuperatorio(), 6.5)

    def test_constructor_valores_limite(self):
        datos = {
            "id_nota": "0",
            "id_materia": "0",
            "valor_nota": "0.0",
            "valor_recuperatorio": "0.0"
        }
        parcial = Parcial(datos)
        self.assertEqual(parcial.get_id_nota(), 0)
        self.assertEqual(parcial.get_id_materia(), 0)
        self.assertEqual(parcial.get_valor_nota(), 0.0)
        self.assertEqual(parcial.get_valor_recuperatorio(), 0.0)

    def test_constructor_herencia_con_error_en_nota(self):
        datos = {
            "id_nota": "xyz",  # Esto debería fallar y quedar como None
            "id_materia": "105",
            "valor_nota": "7.0",
            "valor_recuperatorio": "6.0"
        }
        parcial = Parcial(datos)
        self.assertIsNone(parcial.get_id_nota())
        self.assertEqual(parcial.get_id_materia(), 105)
        self.assertEqual(parcial.get_valor_nota(), 7.0)
        self.assertEqual(parcial.get_valor_recuperatorio(), 6.0)

if __name__ == '__main__':
    unittest.main()
