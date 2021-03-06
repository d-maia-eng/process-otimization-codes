# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:49:21 2021

@author: domin
"""
from random import random
import numpy as np
import matplotlib.pylab as pl

# defina a função objetivo
fobj = lambda x: (1.0/1000.0)*(x+10)*(x+6)*(x+5)*(x+1)*(x-7)*(x-10)

# Defina os limites superiores e inferiores
xmin = -10.0
xmax = 10.0
# Range para plotagem da fobj
xr = np.arange(xmin,xmax, 0.01)
fr = fobj(xr)
#----------------------------------------------------------------------------- 
#         Alcoritmo Genético Condificação Real
#----------------------------------------------------------------------------- 
#
# Defina o melhor valor da função - fbest
fbest = 1.0e8
# Defina o parâmetro eta:
eta = 2
# Defina o número da população e o número de iterações
npop = 10 #numero de individuos
niter = 4 #numero de geraçoes
# Inicialize as variáveis como zero
x=np.zeros(npop)
xnew=np.zeros(npop)
xmut = np.zeros(npop)
# Inicio dos loops
l = 0
i = 0
k = 0
j = 0
while(l<niter):
    # Gerando a população inicial
    for i in range(0,npop):
        alfa = random()
        x[i]= xmin + alfa*(xmax - xmin)
        f = fobj(x[i])
        if (f < fbest):
            xbest = x[i]
            fbest = f
            #classificação

    # Etapa de cruzamento
    if alfa <= 0.5:
        beta = (2.0*alfa)**(1.0/(eta + 1.0))
    else:
        beta = (1.0/(2.0*(1.0 - alfa)))**(1.0/(eta + 1.0))
    for k in range(0,npop):
        xnew[k] = 0.5*((1+beta)*x[k] + (1-beta)*x[npop-1-k])
        if (xnew[k] < xmin):
            xnew[k] = xmin
        if (xnew[k] > xmax):
            xnew[k] = xmax
            
        fnew = fobj(xnew[k])
        if (fnew < fbest):
            xbest = xnew[k]
            fbest = fnew
    
    # Etapa de mutação:        
    for j in range(0,npop):
        xmut[j] = x[j] + alfa*(xmax - xmin)
        #xmut[j]=xnew[j] + alfa*(xmax-xmin)
        if (xmut[j] < xmin):
            xmut[j] = xmin
        if (xmut[j] > xmax):
            xmut[j] = xmax
        
        fmut = fobj(xmut[j])
        if (fmut < fbest):
            xbest = xmut[j]
            fbest = fmut
    # plotagem do gráfico
    pl.plot(xr,fr,xbest,fbest,"bo")
    l += 1
# plotagem do gráfico
#pl.plot(xr,fr,xbest,fbest,"bo")
