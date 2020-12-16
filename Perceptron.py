# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:40:55 2020

@author: davi
"""

from random import *
# O random é pra inicializar os pesos com valores aleatórios
pesoInicial1 = random()
pesoInicial2 = random()
entrada1 = int(input('Digite entre 0 e 1'))
entrada2 = int(input('Digite entre 0 e 1'))
#somatoria = (entrada1*pesoInicial1)+(entrada2*pesoInicial2)
erro = 1
while erro != 0:
    if entrada1 == 1 and entrada2 == 1:
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0
    somatoria = (entrada1 * pesoInicial1) + (entrada2 * pesoInicial2)
    if somatoria < 0:#o real é o zero 1 foi so na aula
        resultado = 0
    elif somatoria >= 0:# o real é com 0 1 foi so na aula
        resultado = 1
    print(f'resultado = {resultado}')
    erro = resultadoEsperado - resultado
    print(f'p1 = {pesoInicial1}')
    print( f'p2 = {pesoInicial2}' )
    pesoInicial1 = pesoInicial1 + (0.2*entrada1*erro)
    pesoInicial2 = pesoInicial2 + (0.2 * entrada2 * erro)
    print(f'erro = {erro}')
