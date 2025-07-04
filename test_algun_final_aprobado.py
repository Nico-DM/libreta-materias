import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Algun_Final_Aprobado import Algun_Final_Aprobado
from Dominio.Materias.materia import Materia
from Dominio.Materias.final import Final

class TestAlgunFinalAprobado(unittest.TestCase):
    def setUp(self):
        self.evaluador = Algun_Final_Aprobado()
        self.materia = MagicMock(spec=Materia)
        self.materia.get_nota_min_aprobar.return_value = 6.0

    # --- Casos normales ---
    def test_un_final_aprobado(self):
        final1 = MagicMock(spec=Final)
        final1.get_valor_nota.return_value = 4.0
        final2 = MagicMock(spec=Final)
        final2.get_valor_nota.return_value = 7.0

        datos = Datos(self.materia, [], [final1, final2])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_todos_los_finales_aprobados(self):
        finales = []
        for nota in [7.0, 9.5, 6.1]:
            final = MagicMock(spec=Final)
            final.get_valor_nota.return_value = nota
            finales.append(final)

        datos = Datos(self.materia, [], finales)
        self.assertTrue(self.evaluador.evaluar(datos))

    # --- Casos de error (lógicos: ninguno aprobado) ---
    def test_ningun_final_aprobado(self):
        finales = []
        for nota in [4.0, 5.5, 3.9]:
            final = MagicMock(spec=Final)
            final.get_valor_nota.return_value = nota
            finales.append(final)

        datos = Datos(self.materia, [], finales)
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_sin_finales(self):
        datos = Datos(self.materia, [], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    # --- Casos límite ---
    def test_unico_final_igual_al_limite(self):
        final = MagicMock(spec=Final)
        final.get_valor_nota.return_value = 6.0  # justo el límite

        datos = Datos(self.materia, [], [final])
        self.assertTrue(self.evaluador.evaluar(datos))

    def test_unico_final_justo_bajo_el_limite(self):
        final = MagicMock(spec=Final)
        final.get_valor_nota.return_value = 5.99  # apenas debajo

        datos = Datos(self.materia, [], [final])
        self.assertFalse(self.evaluador.evaluar(datos))

if __name__ == '__main__':
    unittest.main()
