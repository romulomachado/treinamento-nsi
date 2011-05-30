import unittest
from should_dsl import should
from retangulo import Retangulo

class TestExercicio8(unittest.TestCase):

    def setUp(self):
        self.retangulo = Retangulo(3, 10)

    def teste_deve_calcular_area(self):
        self.retangulo.calcular_area() |should| equal_to(30)

    def teste_deve_calcular_perimetro(self):
        self.retangulo.calcular_perimetro() |should| equal_to(26)

    def teste_deve_verificar_se_eh_quadrado(self):
        self.retangulo.eh_quadrado() |should| equal_to(False)
