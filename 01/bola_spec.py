import unittest
from should_dsl import should
from bola import Bola

class TestExercicio1(unittest.TestCase):

    def setUp(self):
        self.bola = Bola('amarela')

    def teste_consultar_cor_da_bola(self):
        self.bola.cor |should| equal_to('amarela')

    def teste_mudar_cor_da_bola(self):
        self.bola.cor = 'vermelha'
        self.bola.cor |should| equal_to('vermelha')

