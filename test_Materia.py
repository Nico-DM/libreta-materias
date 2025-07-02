import unittest
from Dominio.Materias.materia import Materia  # Asegurate que la ruta sea correcta

class TestMateria(unittest.TestCase):

    def setUp(self):
        self.datos_validos = {
            "id_materia": "1",
            "nombre_materia": "Matemática",
            "nombre_docente": "Prof. Gómez",
            "nota_min_aprobar": "4.0",
            "es_promocionable": True,
            "nota_min_promocion": "7.0",
            "cant_veces_final_rendible": "3",
            "cant_parciales": "2"
        }

    def test_constructor_valores_validos(self):
        materia = Materia(self.datos_validos)
        self.assertEqual(materia.get_id_materia(), 1)
        self.assertEqual(materia.get_nombre_materia(), "Matemática")
        self.assertEqual(materia.get_nombre_docente(), "Prof. Gómez")
        self.assertEqual(materia.get_nota_min_aprobar(), 4.0)
        self.assertTrue(materia.get_es_promocionable())
        self.assertEqual(materia.get_nota_min_promocion(), 7.0)
        self.assertEqual(materia.get_cant_veces_final_rendible(), 3)
        self.assertEqual(materia.get_cant_parciales(), 2)

    def test_constructor_sin_nota_min_promocion(self):
        datos = self.datos_validos.copy()
        datos.pop("nota_min_promocion")
        materia = Materia(datos)
        self.assertIsNone(materia.get_nota_min_promocion())

    def test_constructor_con_nota_min_promocion_invalida(self):
        datos = self.datos_validos.copy()
        datos["nota_min_promocion"] = "no_numero"
        materia = Materia(datos)
        self.assertIsNone(materia.get_nota_min_promocion())

    def test_setters_y_getters(self):
        materia = Materia(self.datos_validos)
        materia.set_id_materia(5)
        self.assertEqual(materia.get_id_materia(), 5)

        materia.set_nombre_materia("Física")
        self.assertEqual(materia.get_nombre_materia(), "Física")

        materia.set_nombre_docente("Prof. Pérez")
        self.assertEqual(materia.get_nombre_docente(), "Prof. Pérez")

        materia.set_nota_min_aprobar(5.0)
        self.assertEqual(materia.get_nota_min_aprobar(), 5.0)

        materia.set_es_promocionable(False)
        self.assertFalse(materia.get_es_promocionable())

        materia.set_nota_min_promocion(8.0)
        self.assertEqual(materia.get_nota_min_promocion(), 8.0)

        materia.set_cant_veces_final_rendible(4)
        self.assertEqual(materia.get_cant_veces_final_rendible(), 4)

        materia.set_cant_parciales(3)
        self.assertEqual(materia.get_cant_parciales(), 3)

    def test_constructor_valores_limite(self):
        datos = {
            "id_materia": "0",
            "nombre_materia": "",
            "nombre_docente": "",
            "nota_min_aprobar": "0.0",
            "es_promocionable": False,
            "nota_min_promocion": "0.0",
            "cant_veces_final_rendible": "0",
            "cant_parciales": "0"
        }
        materia = Materia(datos)
        self.assertEqual(materia.get_id_materia(), 0)
        self.assertEqual(materia.get_nombre_materia(), "")
        self.assertEqual(materia.get_nombre_docente(), "")
        self.assertEqual(materia.get_nota_min_aprobar(), 0.0)
        self.assertFalse(materia.get_es_promocionable())
        self.assertEqual(materia.get_nota_min_promocion(), 0.0)
        self.assertEqual(materia.get_cant_veces_final_rendible(), 0)
        self.assertEqual(materia.get_cant_parciales(), 0)

    def test_constructor_tipos_invalidos_obligatorios(self):
        with self.assertRaises(ValueError):
            Materia({
                "id_materia": "a",
                "nombre_materia": "Historia",
                "nombre_docente": "Prof. León",
                "nota_min_aprobar": "4",
                "es_promocionable": True,
                "nota_min_promocion": "6",
                "cant_veces_final_rendible": "2",
                "cant_parciales": "1"
            })

        with self.assertRaises(ValueError):
            Materia({
                "id_materia": "1",
                "nombre_materia": "Historia",
                "nombre_docente": "Prof. León",
                "nota_min_aprobar": "nota",
                "es_promocionable": True,
                "nota_min_promocion": "6",
                "cant_veces_final_rendible": "2",
                "cant_parciales": "1"
            })

if __name__ == '__main__':
    unittest.main()
