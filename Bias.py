from random import *
pesoInicial1 = random()
pesoInicial2 = random()
pesoBias = random()
entrada1 = int(input('Digite entre 0 e 1:\n'))
entrada2 = int(input('Digite entre 0 e 1:\n'))
Bias = 1
erro = 1
while erro != 0:
    if entrada1 == 1 and entrada2 == 1:
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0
    somatoria = (entrada1 * pesoInicial1) + (entrada2 * pesoInicial2)+(pesoBias*Bias)
    if somatoria < 0:
        resultado = 0
    elif somatoria >= 0:
        resultado = 1
    print(f'resultado = {resultado}')
    erro = resultadoEsperado-resultado
    print(f'p1 = {pesoInicial1}')
    print( f'p2 = {pesoInicial2}' )
    print( f'pb = {pesoBias}' )
    pesoInicial1 = pesoInicial1 + (0.1 * entrada1*erro)
    pesoInicial2 = pesoInicial2 + (0.1 * entrada2 * erro)
    pesoBias = pesoBias + (0.1*Bias*erro)
    print(f'erro = {erro}')