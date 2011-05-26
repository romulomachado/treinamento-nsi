import unittest
from should_dsl import should
from retangulo import Retangulo

class TestRetangulo(unittest.TestCase):

    def setUp(self):
        self.retangulo = Retangulo(5, 2)

    def teste_consultar_lados_do_retangulo(self):
        self.retangulo.base |should| equal_to(5)
        self.retangulo.altura |should| equal_to(2)

    def teste_alterar_lados_do_retangulo(self):
        self.retangulo.alterar_lados(6, 3)
        self.retangulo.base |should| equal_to(6)
        self.retangulo.altura |should| equal_to(3)

    def teste_calcular_area_do_retangulo(self):
        self.retangulo.calcular_area() |should| equal_to(10)

    def teste_calcular_perimetro_do_retangulo(self):
        self.retangulo.calcular_perimetro() |should| equal_to(14)
