import unittest
from should_dsl import should
from conta import Conta

class TestExercicio6(unittest.TestCase):

    def setUp(self):
        self.conta = Conta('Astrobaldo', 123, 100.00)

    def teste_consultar_dados_de_uma_conta(self):
        self.conta.dados |should| equal_to(['Astrobaldo', 123, 100.00])

    def teste_sacar_valor_disponivel_de_uma_conta(self):
        self.conta.sacar(50)
        self.conta.dados[2] |should| equal_to(50.0)

    def teste_sacar_valor_nao_disponivel_de_uma_conta(self):
        self.conta.sacar(200) |should| equal_to("Saldo insuficiente!")
        self.conta.dados[2] |should| equal_to(100)

    def teste_depositar_cinquenta_reais_em_uma_conta(self):
        self.conta.depositar(50)
        self.conta.dados[2] |should| equal_to(150)
