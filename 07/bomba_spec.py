import unittest
from should_dsl import should
from bomba import Bomba, QuantidadeNaoSuportada

class TestExercicio7(unittest.TestCase):

    def setUp(self):
        self.bomba = Bomba(50, 2.90)
        self.bomba.encher_bomba()

    def teste_deve_consultar_quantidade_de_combustivel(self):
        self.bomba.quantidade |should| equal_to(50)

    def teste_deve_abastecer_por_valor(self):
        self.bomba.abastecer_por_valor(29) |should| equal_to(10)

    def teste_deve_encher_bomba_e_retornar_quantidade_de_combustivel_adicionada(self):
        self.bomba.abastecer_por_litro(40)
        self.bomba.encher_bomba() |should| equal_to(40)

    def teste_deve_abastecer_por_litro(self):
        self.bomba.abastecer_por_litro(10) |should| equal_to(29.0)
        self.bomba.quantidade |should| equal_to(40)

    def teste_nao_deve_abastecer_quantidade_litros_maior_que_a_disponivel(self):
        def abastecer_100_litros():
            self.bomba.abastecer_por_litro(100)
        abastecer_100_litros |should| throw(QuantidadeNaoSuportada)

    def teste_nao_deve_abastecer_quantidade_litros_maior_que_a_disponivel_por_valor(self):
        def abastecer_290_reais():
            self.bomba.abastecer_por_valor(290)
        abastecer_290_reais |should| throw(QuantidadeNaoSuportada)
