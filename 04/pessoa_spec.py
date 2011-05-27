import unittest
from should_dsl import should
from pessoa import Pessoa


class TestExercicio4(unittest.TestCase):

    def setUp(self):
        self.pessoa = Pessoa(19, 85, 1.70)

    def teste_consultar_dados_de_uma_pessoa(self):
        self.pessoa.dados |should| equal_to([19, 85, 1.70])

    def teste_alterar_dados_de_uma_pessoa(self):
        self.pessoa.dados = [20, 87, 1.80]
        self.pessoa.dados |should| equal_to([20, 87, 1.80])
