#Atividade 01 - Diana Maia

import numpy as np
from scipy.optimize import minimize

#modelo de ajuste
def Umod(x,Ft):
    p0 = x[0]
    p1 = x[1]
    p2 = x[2]
    return (1.0/((1.0/p0) + (1.0/(p1*Ft**p2))))

#função objetivo minimos quadrados

def f(x):
    #dados experimentais
    nexp = 15
    Uexp = np.array ([46.316,43.308,46.917,55.038,61.053,60.451,59.549,66.466,71.278,76.391,74.887,80.301,79.699,81.805,84.511])
    Ft = np.array ([38.864,43.722,56.972,57.855,62.713,68.896,76.845,86.120,77.287,92.303,104.230,107.320,116.590,126.310,117.920])
    Ft = Ft*1.0e-3

#geração da funçao objetivo

    soma = 0.0
    for i in range(0,nexp):
        soma = soma + (Uexp[i] - Umod(x,Ft[i]))**2
    return soma

#chamando a função objetivo e minimizando via CG

res = minimize(f, [10.0,0.05,1.0], method="CG", tol = 1.0e-5)

print(res) 