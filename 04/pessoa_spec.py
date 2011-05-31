import unittest
from should_dsl import should
from pessoa import Pessoa


class TestExercicio4(unittest.TestCase):

    def setUp(self):
        self.pessoa = Pessoa(19, 85, 170)

    def teste_consultar_dados_de_uma_pessoa(self):
        self.pessoa.dados |should| equal_to([19, 85, 170])

    def teste_alterar_dados_de_uma_pessoa(self):
        self.pessoa.dados = [20, 87, 180]
        self.pessoa.dados |should| equal_to([20, 87, 180])

    def teste_pessoa_deve_engordar_3_quilos(self):
        self.pessoa.engordar(3)
        self.pessoa.dados[1] |should| equal_to(88)

    def teste_pessoa_deve_emagrecer_5_quilos(self):
        self.pessoa.emagrecer(5)
        self.pessoa.dados[1] |should| equal_to(80)
