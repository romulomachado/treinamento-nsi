#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Retangulo:

    def __init__(self, base, altura):
        self.lados = [base, altura]

    def calcular_area(self):
        return self.lados[0] * self.lados[1]

    def calcular_perimetro(self):
        return self.lados[0] * 2 + self.lados[1] * 2
