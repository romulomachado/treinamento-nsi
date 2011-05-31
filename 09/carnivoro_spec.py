import unittest
from should_dsl import should
from carnivoro import Carnivoro

class TestExercicio9(unittest.TestCase):

    def setUp(self):
        self.carnivoro = Carnivoro()

    def teste_deve_comer_qualquer_coisa_e_consultar_estomago(self):
        booleano, numero, palavra, objeto = True, 1, 'treinamento', Carnivoro()
        self.carnivoro.comer(booleano)
        self.carnivoro.comer(numero)
        self.carnivoro.comer(palavra)
        self.carnivoro.comer(objeto)
        self.carnivoro.estomago |should| equal_to([True, 1, 'treinamento', objeto])

    def teste_deve_digerir_alimento_mais_antigo(self):
        booleano, numero, = False, 20
        self.carnivoro.comer(booleano)
        self.carnivoro.comer(numero)
        self.carnivoro.estomago |should| equal_to([False, 20])
        self.carnivoro.digerir()
        self.carnivoro.estomago |should| equal_to([20])
