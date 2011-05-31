import unittest
from should_dsl import should
from numero import Numero

class TestExercicio12(unittest.TestCase):

    def setUp(self):
        self.numero = Numero(13)

    def teste_numero_eh_par(self):
        self.numero.eh_par() |should| equal_to(False)

    def teste_numero_eh_impar(self):
        self.numero.eh_impar() |should| equal_to(True)

    def teste_deve_retornar_forma_romana_do_numero(self):
        self.numero.romano() |should| equal_to("XIII")

    def teste_deve_retornar_fatorial_do_numero_pela_maneira_classica(self):
        self.numero.valor = 5
        self.numero.fatorial_maneira_classica() |should| equal_to(120)

    def teste_deve_retornar_fatorial_do_numero_pela_maneira_recursiva(self):
        self.numero.valor = 4
        self.numero.fatorial_recursivo() |should| equal_to(24)

    def teste_deve_retornar_fatorial_do_numero_pela_maneira_metaprogramatica(self):
        self.numero.valor = 3
        self.numero.fatorial_metaprogramatico() |should| equal_to(6)
