import unittest
from should_dsl import should
from televisao import *


class TestExercicio5(unittest.TestCase):

    def setUp(self):
        self.televisao = Televisao()

    def teste_deve_ligar_tv(self):
        self.televisao.liga_desliga_tv()
        self.televisao.status |should| equal_to(True)

    def teste_deve_desligar_tv(self):
        self.televisao.status = True
        self.televisao.liga_desliga_tv()
        self.televisao.status |should| equal_to(False)

    def teste_consultar_numero_canal(self):
        self.televisao.canal_atual |should| equal_to(2)

    def teste_consultar_volume(self):
        self.televisao.volume_atual |should| equal_to(20)

    def teste_aumentar_volume(self):
        self.televisao.aumentar_volume()
        self.televisao.volume_atual |should| equal_to(21)

    def teste_aumentar_volume_valor_invalido(self):
        self.televisao.volume_atual = 99
        def aumentar_volume():
            self.televisao.aumentar_volume()
        aumentar_volume |should| throw(VolumeMaximoAtingido)

    def teste_diminuir_volume(self):
        self.televisao.diminuir_volume()
        self.televisao.volume_atual |should| equal_to(19)

    def teste_diminuir_volume_valor_invalido(self):
        self.televisao.volume_atual = 0
        def diminuir_volume():
            self.televisao.diminuir_volume()
        diminuir_volume |should| throw(VolumeMinimoAtingido)

    def teste_passar_canal(self):
        self.televisao.passar_canal()
        self.televisao.canal_atual |should| equal_to(3)

    def teste_passar_canal_valor_invalido(self):
        self.televisao.canal_atual = 180
        def passar_canal():
            self.televisao.passar_canal()
        passar_canal |should| throw(FimDosCanais)
        self.televisao.canal_atual |should| equal_to(2)

    def teste_voltar_canal(self):
        self.televisao.canal_atual = 30
        self.televisao.voltar_canal()
        self.televisao.canal_atual |should| equal_to(29)

    def teste_voltar_canal_valor_invalido(self):
        def voltar_canal():
            self.televisao.voltar_canal()
        voltar_canal |should| throw(InicioDosCanais)
        self.televisao.canal_atual |should| equal_to(180)
