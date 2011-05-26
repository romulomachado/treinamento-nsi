import unittest
from should_dsl import should
from quadrado import Quadrado

class TestExercicio2(unittest.TestCase):

    def setUp(self):
        self.quadrado = Quadrado(10)

    def teste_consultar_lado_do_quadrado(self):
        self.quadrado.get_lado() |should| equal_to(10)

    def teste_alterar_lado_do_quadrado(self):
        self.quadrado.set_lado(20)
        self.quadrado.get_lado() |should| equal_to(20)

    def teste_calcular_area_do_quadrado(self):
        self.quadrado.calcular_area() |should| equal_to(100)
