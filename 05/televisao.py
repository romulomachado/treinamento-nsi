#!/usr/bin/env python
#-*- coding:utf-8 -*-

class VolumeMaximoAtingido(Exception):
    pass

class VolumeMinimoAtingido(Exception):
    pass

class FimDosCanais(Exception):
    pass

class InicioDosCanais(Exception):
    pass

class Televisao(object):

    def __init__(self):
        self.canal_atual = 2
        self.volume_atual = 20
        self.status = False

    def liga_desliga_tv(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True

    def aumentar_volume(self):
        if self.volume_atual < 99:
            self.volume_atual += 1
        else:
            raise VolumeMaximoAtingido('Volume maximo atingido!')

    def diminuir_volume(self):
        if self.volume_atual > 0:
            self.volume_atual -= 1
        else:
            raise VolumeMinimoAtingido('Volume minimo atingido!')

    def passar_canal(self):
        if self.canal_atual < 180:
            self.canal_atual += 1
        else:
            self.canal_atual = 2
            raise FimDosCanais('Fim dos canais')

    def voltar_canal(self):
        if self.canal_atual > 2:
            self.canal_atual -= 1
        else:
            self.canal_atual = 180
            raise InicioDosCanais('Inicio dos canais')
