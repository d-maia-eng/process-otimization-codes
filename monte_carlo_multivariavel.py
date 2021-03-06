#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:54:52 2021

@author: gigi
"""
import numpy as np
#import matplotlib.pylab as pl
import matplotlib.pyplot as pl
from random import random
#from mpl_toolkits.mplot3d import Axes3D 

tol = 1.0e-6
niter = 10000

lbx = -10
ubx = 10
lby = -10
uby = 10

def fobj(x,y):
    fx = 100.0*(y - x**2)**2 + (1.0-x)**2  
    return fx
i = 0
#Calculando com o laço while
ftemp = 100000.0
while (i <= niter):
    alfa = random()
    x_atual = lbx + alfa*(ubx-lbx)
    y_atual = lby + alfa*(uby-lby)
    fotimo = fobj(x_atual,y_atual)
    if (fotimo <= ftemp):
        ftemp = fotimo
        xotimo = x_atual
        yotimo = y_atual
        print("f otimo:", fotimo)
        print("x:", x_atual)
        print("y:", y_atual)
        print("iteração:", i)
    i = i + 1
#Chamando a função arange(faixa menor, faixa maior, passo)
#xr = np.arange(lbx,ubx,0.01)
#yr = np.arange(lby,uby,0.01)
#fr = fobj(xr,yr)
#pl.plot(xr,fr,x_atual,fobj(xotimo),"bs")

xlist = np.linspace(lbx, ubx, 100)
ylist = np.linspace(lby, uby, 100)

x, y = np.meshgrid(xlist, ylist)
Z = fobj(x,y)
Zr = fobj(xotimo,yotimo)
fig,ax=pl.subplots(1,1)
cp = ax.contourf(x, y, Z)
#cpr = ax.contourf(xotimo, yotimo, Zr)
#fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot')
#ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')
pl.show()

"""
x = np.linspace(lbx, ubx, 30)
y = np.linspace(lby, uby, 30)

xr, yr = np.meshgrid(x, y)
Z = fobj(xr, yr)
fig = pl.figure()
ax = fig.gca(projection="3d")
ax.plot_surface(xr, yr, Z, rstride=1, cstride=1,cmap="winter", edgecolor="none")
ax.set_title("surface");
pl.show()
#pl.contour("")
"""
