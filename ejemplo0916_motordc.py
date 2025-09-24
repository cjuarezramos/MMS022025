# Autor: Carlos Juarez
# Fecha: 16 de septiembre del 2025
# Descripción: Este programa simula el motor DC

# modulos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del sistema
R = 2.27
L = 0.0047
Ka = 0.25
Km = 0.25
J = 0.00246
B = 0.003026

# Datos de simulacion
h = 1e-4
tf = 10
t = np.arange(0,tf,h)



# funcion a resolver
def f(t,x):
    i = x[0]
    w = x[1]
    Vent = 6
    di_dt = -R/L*i - Ka/L*w + Vent/L
    dw_dt = -B/J*w + Km/J*i
    return [di_dt,dw_dt]

sol = solve_ivp(f,[0,10],[0,0])

print(sol)

plt.plot(sol.t,sol.y[0])
plt.show()
plt.plot(sol.t,sol.y[1])
plt.title('Velocidad del motor DC')
plt.xlabel('Tiempo (s)')
plt.show()