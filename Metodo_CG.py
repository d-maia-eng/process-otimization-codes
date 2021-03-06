# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:43:01 2021

@author: domin
"""
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

#def reporter(p):
#    """Reporter function to capture intermediate states of optimization."""
#    global ps
#    #ps.append(p)

def f(x):   
    #return 100.0*(x[1] - x[0]**2)**2 + (1.0 - x[0])**2
    #return 8.0*x[0]**2 + 4.0*x[0]*x[1] + 5.0*x[1]**2
    return x[0]**3*np.exp(x[1] - x[0]**2 - 10.0*(x[0] - x[1])**2)
     

res = minimize(f, [1, 1], method="CG", tol = 1.0e-5)  #,callback=reporter) 

print(res)

#def jacobian(x):
#    return np.array((-2*.5*(1 - x[0]) - 4*x[0]*(x[1] - x[0]**2), 2*(x[1] - x[0]**2)))
#optimize.minimize(f, [2, 1], method="CG", jac=jacobian)
'''
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(np.vstack([X.ravel(), Y.ravel()])).reshape((100,100))


ps = np.array(res.x)
plt.figure()
plt.contour(X, Y, Z, np.arange(10)**6, cmap='jet')
plt.plot(ps[0], ps[1], '-ro')
'''