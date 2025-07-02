import unittest
from Dominio.Materias.final import Final

class TestFinal(unittest.TestCase):

    def setUp(self):
        self.datos = {
            "id_nota": "1",
            "id_materia": "101",
            "valor_nota": "9.0"
        }

    def test_constructor_valores_validos(self):
        final = Final(self.datos)
        self.assertEqual(final.get_id_nota(), 1)
        self.assertEqual(final.get_id_materia(), 101)
        self.assertEqual(final.get_valor_nota(), 9.0)

    def test_constructor_id_nota_invalido(self):
        datos = self.datos.copy()
        datos["id_nota"] = "abc"
        final = Final(datos)
        self.assertIsNone(final.get_id_nota())
        self.assertEqual(final.get_id_materia(), 101)
        self.assertEqual(final.get_valor_nota(), 9.0)

    def test_setters_y_getters(self):
        final = Final(self.datos)
        final.set_id_nota(5)
        self.assertEqual(final.get_id_nota(), 5)

        final.set_id_materia(202)
        self.assertEqual(final.get_id_materia(), 202)

        final.set_valor_nota(7.5)
        self.assertEqual(final.get_valor_nota(), 7.5)

    def test_constructor_valores_limite(self):
        datos = {
            "id_nota": "0",
            "id_materia": "0",
            "valor_nota": "0.0"
        }
        final = Final(datos)
        self.assertEqual(final.get_id_nota(), 0)
        self.assertEqual(final.get_id_materia(), 0)
        self.assertEqual(final.get_valor_nota(), 0.0)

    def test_constructor_valores_invalidos(self):
        with self.assertRaises(ValueError):
            Final({
                "id_nota": "1",
                "id_materia": "no es int",
                "valor_nota": "9.0"
            })

        with self.assertRaises(ValueError):
            Final({
                "id_nota": "1",
                "id_materia": "101",
                "valor_nota": "nueve"
            })

if __name__ == '__main__':
    unittest.main()
