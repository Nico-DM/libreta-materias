import unittest
from unittest.mock import Mock
from Dominio.Funciones_sistema.Logica_negocio.determinador_estado import Determinador_Estado
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Materias.datos import Datos

class TestDeterminadorEstado(unittest.TestCase):

    def setUp(self):
        self.datos_mock = Mock(spec=Datos)

    def mock_evaluaciones(self, resultados: list[bool]):
        evaluaciones = []
        for resultado in resultados:
            evaluacion = Mock()
            evaluacion.evaluar.return_value = resultado
            evaluaciones.append(evaluacion)
        return evaluaciones

    def test_devuelve_cursando_si_evaluacion_cursando_true(self):
        cursando = self.mock_evaluaciones([True])
        estado = Determinador_Estado(
            evaluaciones_cursando=cursando,
            evaluaciones_promociono=self.mock_evaluaciones([True]),
            evaluaciones_aprobo=self.mock_evaluaciones([True]),
            evaluaciones_regularizo=self.mock_evaluaciones([True])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.CURSANDO)

    def test_devuelve_promocionado_si_solo_promocion_true(self):
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([False]),
            evaluaciones_promociono=self.mock_evaluaciones([True, True]),
            evaluaciones_aprobo=self.mock_evaluaciones([False]),
            evaluaciones_regularizo=self.mock_evaluaciones([False])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.PROMOCIONADO)

    def test_devuelve_aprobado_si_solo_aprobado_true(self):
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([False]),
            evaluaciones_promociono=self.mock_evaluaciones([False]),
            evaluaciones_aprobo=self.mock_evaluaciones([True]),
            evaluaciones_regularizo=self.mock_evaluaciones([False])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.APROBADO)

    def test_devuelve_regularizado_si_solo_regularizo_true(self):
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([False]),
            evaluaciones_promociono=self.mock_evaluaciones([False]),
            evaluaciones_aprobo=self.mock_evaluaciones([False]),
            evaluaciones_regularizo=self.mock_evaluaciones([True, True])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.REGULARIZADO)

    def test_devuelve_desaprobado_si_todo_falso(self):
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([False]),
            evaluaciones_promociono=self.mock_evaluaciones([False]),
            evaluaciones_aprobo=self.mock_evaluaciones([False]),
            evaluaciones_regularizo=self.mock_evaluaciones([False])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.DESAPROBADO)

    def test_prioridad_orden_correcto(self):
        # Todos los evaluadores devuelven True, pero debe devolver CURSANDO por prioridad
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([True]),
            evaluaciones_promociono=self.mock_evaluaciones([True]),
            evaluaciones_aprobo=self.mock_evaluaciones([True]),
            evaluaciones_regularizo=self.mock_evaluaciones([True])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.CURSANDO)

    def test_falla_uno_en_cadena_y_no_pasa(self):
        # Una sola evaluación cursando es False => no CURSANDO
        estado = Determinador_Estado(
            evaluaciones_cursando=self.mock_evaluaciones([True, False]),
            evaluaciones_promociono=self.mock_evaluaciones([True]),
            evaluaciones_aprobo=self.mock_evaluaciones([False]),
            evaluaciones_regularizo=self.mock_evaluaciones([False])
        ).determinar_estado(self.datos_mock)
        self.assertEqual(estado, Estado.PROMOCIONADO)

if __name__ == '__main__':
    unittest.main()
