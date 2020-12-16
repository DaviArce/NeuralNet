import numpy as np 
import matplotlib.pyplot as plt
#
def sigmoid(x):
    return 1/(1 + np.exp(-x))
x = np.array([1,2,3,4,5])
y = sigmoid(x)
#
def derivadaParcial(vsig):
    return vsig*(1-vsig)
dev = derivadaParcial(0.5)
#
def deltaSaida(erro,dev):
    return erro*dev
erro = 0.5
deltaS=deltaSaida(erro,dev)
#
def deltaEscondida(derivada,peso,deltaS):
    return derivada*peso*deltaS
peso = 0.5
deltaE = deltaEscondida(dev,peso,deltaS)
def AtualizaPeso(peso,entrada,delta,alpha):
    return (peso*1)+(entrada*delta*alpha)
Npeso1 = AtualizaPeso(0.3,0.9,deltaS,0.5)
Npeso = AtualizaPeso(0.2,0.5,deltaS,0.5)

NpesoO1 = AtualizaPeso(0.5,1,deltaE,0.5)
NpesoO2 = AtualizaPeso()





