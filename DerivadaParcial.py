import numpy as np 
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1/(1 + np.exp(-x))
x = np.array([1,2,3,4,5])
y = sigmoid(x)
def derivadaParcial(vsig):
    return vsig*(1-vsig)
dev = derivadaParcial(y)



