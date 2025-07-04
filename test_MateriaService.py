import unittest
from unittest.mock import MagicMock, Mock
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.final import Final
from api.materia_service import MateriaService

class TestMateriaService(unittest.TestCase):

    def setUp(self):
        self.handlers = {
            "materia": MagicMock(),
            "parcial": MagicMock(),
            "final": MagicMock(),
            "repo": MagicMock()
        }
        self.determiner = MagicMock()
        self.service = MateriaService(self.determiner, self.handlers)

        self.datos_materia = {
            "id_materia": 1,
            "nombre_materia": "Álgebra",
            "nombre_docente": "Juan",
            "nota_min_aprobar": 6.0,
            "nota_min_promocion": 8.0,
            "es_promocionable": True,
            "cant_veces_final_rendible": 3,
            "cant_parciales": 2
        }

    # --- Casos normales ---
    def test_crear_materia(self):
        materia = self.service.crear_materia(self.datos_materia)
        self.handlers["materia"].agregar.assert_called_once()
        self.assertIsInstance(materia, Materia)

    def test_obtener_materias(self):
        self.handlers["materia"].obtener_todas.return_value = ["materia1", "materia2"]
        materias = self.service.obtener_materias()
        self.assertEqual(materias, ["materia1", "materia2"])

    def test_eliminar_materia(self):
        self.service.eliminar_materia(1)
        self.handlers["materia"].eliminar.assert_called_once_with(1)

    def test_modificar_materia(self):
        self.service.modificar_materia(1, "nombre_materia", "Análisis")
        self.handlers["materia"].modificar.assert_called_once_with(1, "nombre_materia", "Análisis")

    def test_agregar_parcial(self):
        parcial = self.service.agregar_parcial(1, 7.0)
        self.handlers["parcial"].agregar.assert_called_once()
        self.assertIsInstance(parcial, Parcial)
        self.assertEqual(parcial.get_valor_nota(), 7.0)

    def test_modificar_parcial(self):
        self.service.modificar_parcial(10, "valor_nota", 8.5)
        self.handlers["parcial"].modificar.assert_called_once_with(10, "valor_nota", 8.5)

    def test_agregar_final(self):
        final = self.service.agregar_final(1, 9.0)
        self.handlers["final"].agregar.assert_called_once()
        self.assertIsInstance(final, Final)
        self.assertEqual(final.get_valor_nota(), 9.0)

    def test_modificar_final(self):
        self.service.modificar_final(5, "valor_nota", 6.0)
        self.handlers["final"].modificar.assert_called_once_with(5, "valor_nota", 6.0)

    def test_agregar_recuperatorio(self):
        parcial_mock = Mock()
        self.handlers["parcial"].obtener.return_value = parcial_mock
        result = self.service.agregar_recuperatorio(1, 10, 6.0)
        self.handlers["parcial"].agregar_recuperatorio.assert_called_once_with(1, 10, 6.0)
        self.handlers["parcial"].obtener.assert_called_once_with(10)
        self.assertEqual(result, parcial_mock)

    def test_determinar_estado(self):
        materia_mock = Mock()
        parciales_mock = [Mock()]
        finales_mock = [Mock()]
        self.handlers["parcial"].obtener_todas_de.return_value = parciales_mock
        self.handlers["final"].obtener_todas_de.return_value = finales_mock
        self.determiner.determinar_estado.return_value = "PROMOCIONADO"

        estado = self.service.determinar_estado(materia_mock)
        self.assertEqual(estado, "PROMOCIONADO")

    def test_obtener_materia_con_estado_ok(self):
        materia_mock = Mock()
        self.handlers["materia"].obtener.return_value = materia_mock
        self.handlers["parcial"].obtener_todas_de.return_value = []
        self.handlers["final"].obtener_todas_de.return_value = []
        self.determiner.determinar_estado.return_value = "REGULAR"

        materia, estado = self.service.obtener_materia_con_estado(1)
        self.assertEqual(materia, materia_mock)
        self.assertEqual(estado, "REGULAR")

    # --- Casos de error ---
    def test_obtener_materia_con_estado_error(self):
        self.handlers["materia"].obtener.side_effect = Exception("No existe")
        with self.assertRaises(ValueError) as ctx:
            self.service.obtener_materia_con_estado(999)
        self.assertEqual(str(ctx.exception), "Materia no encontrada")

    def test_eliminar_base(self):
        self.service.eliminar_base()
        self.handlers["repo"].eliminar_base.assert_called_once()

    def test_mover_notas(self):
        self.service.mover_notas(1, 2)
        self.handlers["repo"].mover_notas.assert_called_once_with(1, 2)

    # --- Casos límite ---
    def test_crear_materia_con_promocion_none(self):
        datos = self.datos_materia.copy()
        datos["nota_min_promocion"] = None
        materia = self.service.crear_materia(datos)
        self.assertIsNone(materia.get_nota_min_promocion())

    def test_agregar_parcial_valor_minimo(self):
        parcial = self.service.agregar_parcial(1, 0.0)
        self.assertEqual(parcial.get_valor_nota(), 0.0)

    def test_agregar_final_valor_maximo(self):
        final = self.service.agregar_final(1, 10.0)
        self.assertEqual(final.get_valor_nota(), 10.0)

    def test_modificar_materia_valor_extremo(self):
        self.service.modificar_materia(1, "cant_parciales", 1000)
        self.handlers["materia"].modificar.assert_called_once_with(1, "cant_parciales", 1000)


if __name__ == "__main__":
    unittest.main()
