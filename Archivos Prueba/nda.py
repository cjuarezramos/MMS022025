import control as ct
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
wn = 1000
z = 0.1
K=1
J = 0.01
B = 0.02
def f(t,x):
    U = 1
    dx1dt = x[1]
    dx2dt = -B/J*x[1] - K/J*x[0] + K/J*U
    return np.array([dx1dt,dx2dt])
sol = solve_ivp(f,[0,0.1],[0,0])
plt.plot(sol.t,sol.y[0])
plt.show()
num_ol = [K]
den_ol = [J, B, 0]
G = ct.tf(num_ol, den_ol)
# respuesta al escalón del sistema de lazo abierto
# Lugar de las raíces del sistema
ct.root_locus_map(G).plot()
plt.show()