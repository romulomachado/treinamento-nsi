#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Carnivoro(object):

    def __init__(self):
        self.estomago = []

    def comer(self, comida):
        self.estomago.append(comida)

    def digerir(self):
        self.estomago.pop(0)
