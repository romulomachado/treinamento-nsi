#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Conta:
    def __init__(self, dono, numero, saldo = 0.0):
        self.dados = [dono, numero, saldo]

    def sacar(self, valor):
        if self.dados[2] < valor:
            return "Saldo insuficiente!" #TODO: raise Exception
        else:
            self.dados[2] -= valor

    def depositar(self, valor):
        self.dados[2] += valor
