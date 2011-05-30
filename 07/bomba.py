#!/usr/bin/env python
#-*- coding:utf-8 -*-

class QuantidadeNaoSuportada(Exception):
    pass

class Bomba(object):

    def __init__(self, capacidade, preco_por_litro):
        self.capacidade = capacidade
        self.quantidade = 0
        self.preco_por_litro = preco_por_litro

    def encher_bomba(self):
        quantidade_abastecida = self.capacidade - self.quantidade
        self.quantidade = quantidade_abastecida
        return quantidade_abastecida

    def abastecer_por_valor(self, valor):
        quantidade = valor / self.preco_por_litro
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return quantidade
        else:
            raise QuantidadeNaoSuportada('Quantidade nao disponivel na bomba!')

    def abastecer_por_litro(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return quantidade * self.preco_por_litro
        else:
            raise QuantidadeNaoSuportada('Quantidade nao disponivel na bomba!')
