#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Pessoa(object):

    def __init__(self, idade, peso, altura):
        self.dados = [idade, peso, altura]

    def engordar(self, peso_obtido):
        self.dados[1] += peso_obtido

    def emagrecer(self, peso_perdido):
        self.dados[1] -= peso_perdido
