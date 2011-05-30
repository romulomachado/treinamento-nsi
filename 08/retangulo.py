#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Retangulo(object):

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura

    def calcular_perimetro(self):
        return self.altura * 2 + self.largura * 2

    def eh_quadrado(self):
        if self.altura == self.largura:
            return True
        else:
            return False
