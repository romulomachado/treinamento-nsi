import unittest
from should_dsl import should
from bola import Bola

class TestBola(unittest.TestCase):

    def teste_mudar_cor_da_bola(self):
        self.bola = Bola('amarela')
        self.bola.mudar_cor('vermelha')
        self.bola.cor |should| equal_to('vermelha')

