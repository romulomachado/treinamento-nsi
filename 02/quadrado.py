#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Quadrado:

    def __init__(self, tamanho_do_lado):
        self.lado = tamanho_do_lado

    def alterar_tamanho(self, novo_tamanho):
        self.lado = novo_tamanho

    def consultar_tamanho_dos_lados(self):
        return self.lado

    def calcular_area(self):
        return pow(self.lado, 2)
