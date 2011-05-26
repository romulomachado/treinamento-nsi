#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return pow(self.lado, 2)
