import unittest
from unittest.mock import MagicMock, Mock
from api.materia_service import MateriaService
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final
from Dominio.Materias.datos import Datos

class TestMateriaController(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.determinador_estado = MagicMock()
        self.materia_service = MateriaService(self.repo, self.determinador_estado)
        self.datos_materia = {
            "id_materia": 1,
            "nombre_materia": "Álgebra",
            "nombre_docente": "Juan",
            "cant_parciales": 2,
            "nota_min_aprobar": 6,
            "nota_min_promocion": 8,
            "es_promocionable": True,
            "cant_veces_final_rendible": 5
        }

    def test_crear_materia(self):
        materia = self.materia_service.crear_materia(self.datos_materia)
        self.repo.agregar_materia.assert_called_once_with(materia)
        self.assertIsInstance(materia, Materia)
        self.assertEqual(materia.get_nombre_materia(), "Álgebra")

    def test_agregar_parcial(self):
        parcial = self.materia_service.agregar_parcial(self.datos_materia["id_materia"], 6.0)
        self.repo.agregar_parcial.assert_called_once()
        self.assertIsInstance(parcial, Parcial)
        self.assertEqual(parcial.get_valor_nota(), 6.0)

    def test_agregar_final(self):
        final = self.materia_service.agregar_final(self.datos_materia["id_materia"], 7.0)
        self.repo.agregar_final.assert_called_once()
        self.assertIsInstance(final, Final)
        self.assertEqual(final.get_valor_nota(), 7.0)

    def test_agregar_recuperatorio(self):
        parcial_mock = Mock()
        self.repo.obtener_parcial.return_value = parcial_mock
        resultado = self.materia_service.agregar_recuperatorio(self.datos_materia["id_materia"], 10, 8.0)
        self.repo.agregar_recuperatorio.assert_called_once_with(self.datos_materia["id_materia"], 10, 8.0)
        self.repo.obtener_parcial.assert_called_once_with(10)
        self.assertEqual(resultado, parcial_mock)

    def test_obtener_materia_con_estado_ok(self):
        materia_mock = Mock()
        parciales_mock = [Mock()]
        finales_mock = [Mock()]
        estado_mock = "PROMOCIONADO"

        self.repo.obtener_materia.return_value = materia_mock
        self.repo.obtener_parciales.return_value = parciales_mock
        self.repo.obtener_finales.return_value = finales_mock
        self.determinador_estado.determinar_estado.return_value = estado_mock

        materia, estado = self.materia_service.obtener_materia_con_estado(self.datos_materia["id_materia"])

        self.repo.obtener_materia.assert_called_once_with(self.datos_materia["id_materia"])
        self.repo.obtener_parciales.assert_called_once_with(materia_mock)
        self.repo.obtener_finales.assert_called_once_with(materia_mock)
        self.determinador_estado.determinar_estado.assert_called_once()
        self.assertEqual(materia, materia_mock)
        self.assertEqual(estado, estado_mock)

    def test_obtener_materia_con_estado_no_encontrada(self):
        self.repo.obtener_materia.return_value = None
        with self.assertRaises(ValueError) as context:
            self.materia_service.obtener_materia_con_estado(2)
        self.assertEqual(str(context.exception), "Materia no encontrada")

if __name__ == '__main__':
    unittest.main()
