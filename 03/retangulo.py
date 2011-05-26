#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def get_lados(self):
        lados = (self.base, self.altura)
        return lados

    def set_lados(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return self.base * 2 + self.altura * 2
