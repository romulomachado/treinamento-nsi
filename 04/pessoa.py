#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Pessoa(object):

    def __init__(self, idade, peso, altura):
        self.dados = [idade, peso, altura]

    def aniversario(self):
        self.idade += 1
