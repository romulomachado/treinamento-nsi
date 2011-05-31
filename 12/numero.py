#!/usr/bin/env python
#-*- coding:utf-8 -*-


class Numero(object):

    def __init__(self, valor):
        self.valor = valor

    def eh_par(self):
        if self.valor % 2 == 0:
            return True
        return False

    def eh_impar(self):
        if self.valor % 2 != 0:
            return True
        return False

    def romano(self):
        unidades = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
            7: "VII", 8: "VIII", 9: "IX"}
        dezenas = {0: "", 1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX",
            7: "LXX", 8: "LXXX", 9: "XC"}
        return dezenas[self.valor/10] + unidades[self.valor % 10]

    def fatorial_maneira_classica(self):
        fatorial = 1
        for i in range(1, self.valor+1):
            fatorial *= i
        return fatorial

    def fatorial_recursivo(self):
        if self.valor == 1 or self.valor == 0:
            return 1
        return self.valor * Numero(self.valor-1).fatorial_recursivo()

    def fatorial_metaprogramatico(self):
        return reduce (lambda x,y: x*y, range(1,self.valor+1))
