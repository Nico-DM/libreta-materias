import unittest
from Dominio.Materias.nota import Nota

class TestNota(unittest.TestCase):

    def test_constructor_valores_validos(self):
        datos = {"id_nota": "1", "id_materia": "101", "valor_nota": "9.5"}
        nota = Nota(datos)
        self.assertEqual(nota.get_id_nota(), 1)
        self.assertEqual(nota.get_id_materia(), 101)
        self.assertEqual(nota.get_valor_nota(), 9.5)

    def test_constructor_id_nota_invalido(self):
        datos = {"id_nota": "abc", "id_materia": "101", "valor_nota": "7.0"}
        nota = Nota(datos)
        self.assertIsNone(nota.get_id_nota())
        self.assertEqual(nota.get_id_materia(), 101)
        self.assertEqual(nota.get_valor_nota(), 7.0)

    def test_setters_y_getters(self):
        datos = {"id_nota": "2", "id_materia": "202", "valor_nota": "6.0"}
        nota = Nota(datos)

        nota.set_id_nota(10)
        self.assertEqual(nota.get_id_nota(), 10)

        nota.set_id_materia(303)
        self.assertEqual(nota.get_id_materia(), 303)

        nota.set_valor_nota(8.5)
        self.assertEqual(nota.get_valor_nota(), 8.5)

    def test_constructor_valores_limite(self):
        datos = {"id_nota": "0", "id_materia": "0", "valor_nota": "0"}
        nota = Nota(datos)
        self.assertEqual(nota.get_id_nota(), 0)
        self.assertEqual(nota.get_id_materia(), 0)
        self.assertEqual(nota.get_valor_nota(), 0.0)

    def test_constructor_faltan_claves(self):
        datos = {"id_materia": "101", "valor_nota": "7.0"}
        nota = Nota(datos)
        self.assertIsNone(nota.get_id_nota())
        self.assertEqual(nota.get_id_materia(), 101)
        self.assertEqual(nota.get_valor_nota(), 7.0)

    def test_constructor_valores_no_numericos(self):
        with self.assertRaises(ValueError):
            Nota({"id_nota": "1", "id_materia": "abc", "valor_nota": "7.0"})

        with self.assertRaises(ValueError):
            Nota({"id_nota": "1", "id_materia": "101", "valor_nota": "ocho"})

if __name__ == '__main__':
    unittest.main()
