import unittest
from Dominio.Materias.datos import Datos
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final

class TestDatos(unittest.TestCase):

    def setUp(self):
        self.datos_materia = {
            "id_materia": "1",
            "nombre_materia": "Lengua",
            "nombre_docente": "Prof. Díaz",
            "nota_min_aprobar": "4.0",
            "es_promocionable": True,
            "nota_min_promocion": "7.0",
            "cant_veces_final_rendible": "3",
            "cant_parciales": "2"
        }

        self.datos_parcial_1 = {
            "id_nota": "10",
            "id_materia": "1",
            "valor_nota": "5.0",
            "valor_recuperatorio": "6.0"
        }

        self.datos_parcial_2 = {
            "id_nota": "11",
            "id_materia": "1",
            "valor_nota": "7.0",
            "valor_recuperatorio": "None"
        }

        self.datos_final = {
            "id_nota": "20",
            "id_materia": "1",
            "valor_nota": "8.0"
        }

        self.materia = Materia(self.datos_materia)
        self.parcial1 = Parcial(self.datos_parcial_1)
        self.parcial2 = Parcial(self.datos_parcial_2)
        self.final = Final(self.datos_final)

    def test_constructor_con_valores_validos(self):
        datos = Datos(self.materia, [self.parcial1], [self.final])
        self.assertEqual(datos.get_materia().get_id_materia(), 1)
        self.assertEqual(len(datos.get_parciales()), 1)
        self.assertEqual(datos.get_parciales()[0].get_id_nota(), 10)
        self.assertEqual(len(datos.get_finales()), 1)
        self.assertEqual(datos.get_finales()[0].get_valor_nota(), 8.0)

    def test_setters_y_getters(self):
        datos = Datos(self.materia, [], [])
        
        nueva_materia = Materia({
            "id_materia": "2",
            "nombre_materia": "Física",
            "nombre_docente": "Prof. Tesla",
            "nota_min_aprobar": "5.0",
            "es_promocionable": False,
            "nota_min_promocion": "7.5",
            "cant_veces_final_rendible": "2",
            "cant_parciales": "3"
        })
        datos.set_materia(nueva_materia)
        self.assertEqual(datos.get_materia().get_nombre_materia(), "Física")

        datos.set_parciales([self.parcial1, self.parcial2])
        self.assertEqual(len(datos.get_parciales()), 2)
        self.assertEqual(datos.get_parciales()[1].get_id_nota(), 11)

        datos.set_finales([self.final])
        self.assertEqual(len(datos.get_finales()), 1)
        self.assertEqual(datos.get_finales()[0].get_valor_nota(), 8.0)

    def test_constructor_listas_vacias(self):
        datos = Datos(self.materia, [], [])
        self.assertEqual(datos.get_parciales(), [])
        self.assertEqual(datos.get_finales(), [])

    def test_objetos_correctos(self):
        datos = Datos(self.materia, [self.parcial1], [self.final])
        self.assertIsInstance(datos.get_materia(), Materia)
        for p in datos.get_parciales():
            self.assertIsInstance(p, Parcial)
        for f in datos.get_finales():
            self.assertIsInstance(f, Final)

if __name__ == '__main__':
    unittest.main()
