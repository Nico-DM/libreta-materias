import unittest
from unittest.mock import MagicMock
from Dominio.Materias.datos import Datos
from Dominio.Funciones_sistema.Calculos_notas.Evaluaciones.Faltan_Notas_Parcial_o_Recuperatorio import Faltan_Notas_Parcial_o_Recuperatorio
from Dominio.Materias.materia import Materia
from Dominio.Materias.parcial import Parcial

class TestFaltanNotasParcialORecuperatorio(unittest.TestCase):
    def setUp(self):
        self.evaluador = Faltan_Notas_Parcial_o_Recuperatorio()
        self.materia = MagicMock(spec=Materia)
        self.materia.get_cant_parciales.return_value = 2
        self.materia.get_nota_min_aprobar.return_value = 6.0

    # --- Casos normales ---
    def test_parciales_suficientes_todos_aprobados(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 8.0
        parcial1.get_valor_recuperatorio.return_value = None

        parcial2 = MagicMock(spec=Parcial)
        parcial2.get_valor_nota.return_value = 6.0
        parcial2.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [parcial1, parcial2], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_parciales_suficientes_desaprobado_pero_con_recuperatorio(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 4.0
        parcial1.get_valor_recuperatorio.return_value = 6.0  # recuperó

        parcial2 = MagicMock(spec=Parcial)
        parcial2.get_valor_nota.return_value = 7.0
        parcial2.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [parcial1, parcial2], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    # --- Casos de error lógico ---
    def test_faltan_parciales(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 9.0
        parcial1.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [parcial1], [])
        self.assertTrue(self.evaluador.evaluar(datos))  # Falta un parcial

    def test_parcial_desaprobado_sin_recuperatorio(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 5.0
        parcial1.get_valor_recuperatorio.return_value = None

        parcial2 = MagicMock(spec=Parcial)
        parcial2.get_valor_nota.return_value = 7.0
        parcial2.get_valor_recuperatorio.return_value = None

        datos = Datos(self.materia, [parcial1, parcial2], [])
        self.assertTrue(self.evaluador.evaluar(datos))  # Desaprobado sin recuperar

    # --- Casos límite ---
    def test_parcial_justo_en_limite_y_otra_con_recuperatorio(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 6.0  # justo el mínimo
        parcial1.get_valor_recuperatorio.return_value = None

        parcial2 = MagicMock(spec=Parcial)
        parcial2.get_valor_nota.return_value = 4.0
        parcial2.get_valor_recuperatorio.return_value = 6.0  # recupera bien

        datos = Datos(self.materia, [parcial1, parcial2], [])
        self.assertFalse(self.evaluador.evaluar(datos))

    def test_todos_desaprobados_pero_recuperados(self):
        parcial1 = MagicMock(spec=Parcial)
        parcial1.get_valor_nota.return_value = 3.0
        parcial1.get_valor_recuperatorio.return_value = 7.0

        parcial2 = MagicMock(spec=Parcial)
        parcial2.get_valor_nota.return_value = 2.0
        parcial2.get_valor_recuperatorio.return_value = 6.5

        datos = Datos(self.materia, [parcial1, parcial2], [])
        self.assertFalse(self.evaluador.evaluar(datos))  # Aunque todos desaprobaron, recuperaron

if __name__ == '__main__':
    unittest.main()
