#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Quadrado:

    def __init__(self, tamanho_do_lado):
        self.lado = tamanho_do_lado

    def get_lado(self):
        return self.lado

    def set_lado(self, novo_tamanho):
        self.lado = novo_tamanho

    def calcular_area(self):
        return pow(self.lado, 2)
