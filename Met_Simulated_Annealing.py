# -*- coding: utf-8 -*-
from random import random
import numpy as np
import matplotlib.pylab as pl

# defina a função objetivo
def fobj(x):
    return (1.0/1000.0)*(x+10)*(x+6)*(x+5)*(x+1)*(x-7)*(x-10)

#-----------------------------------------------------------------------------
# Simulated Annealing
#-----------------------------------------------------------------------------
# Defina o número de iterações e o número de reduções de temperatura.
Ntemp = 20
Niter = 100
# Defina os limites superiores e inferiores
xmin = -10.0
xmax = 10.0
# Range para plotagem da fobj
xr = np.arange(xmin,xmax, 0.1)
fr = fobj(xr)
#   Loop de otimização
#
# Calcule o valor do parâmetro de redução linear
alfa = 0.80
# Calcule um valor de x de forma aleatória
gama = random()  # número aleatório entre 0 e 1
x = xmin + gama*(xmax - xmin)
# Calcule o valor da função objetivo:
fold = fobj(x)
# Faça fotimo igual a fold:
xotm = x
fotm = fold
# Valo inicial da iteração
i = 1           # contador de iterações
iTemp = 1       # contador da temperatura    
# Loop de redução de temperatura:
while(iTemp <= Ntemp):
    while (i <= Niter):        
        # Atualize a iteração:
        i+=1
        #print(i)
        # Gere uma nova solução de forma aleatório
        gama = random()  # número aleatório entre 0 e 1
        xnew = xmin + gama*(xmax - xmin) #(1.0 + gama)*x
        # Calcule o novo valor da função objetivo
        fnew = fobj(xnew)
        # Calcule o valor da diferença entre as funções - delta
        delta = fnew - fold
        # Avalie a energia
        if (delta < 0.0):
            x = xnew
            fold = fnew
            if (fnew < fotm):
                xotm = xnew
                fotm = fnew
                print(xotm,fotm)
                # Plotando os resultados
                pl.plot(xr,fr,xotm,fotm,"ro")
        else:
            beta = np.exp(-delta/(2*fold))
            alfa1 = random()
            if ( beta > alfa1):
                x = xnew
                fold = fnew
                #x = alfa*x
    # Atualização do passo de temperatura
    i = 1
    x = alfa*x
    iTemp += iTemp
    #print(iTemp)

pl.show()




   


    
            