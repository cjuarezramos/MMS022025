import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del sistema
m1 = 1.0  # masa 1
m2 = 1.0  # masa 2
k1 = 1.0  # constante del resorte 1
k2 = 1.0  # constante del resorte 2
c = 0.5   # coeficiente de amortiguamiento
g = 9.81  # aceleración debida a la gravedad

def f(t, x):
    z1 = x[0]
    v1 = x[1]
    z2 = x[2]
    v2 = x[3]
    r = 1
    dz1dt = v1
    dv1dt = (-c*v1-(k1+k2)*z1+c*v2 + k2*z2 - m1*g + r*k2)/m1
    dz2dt = v2
    dv2dt = (-c*v2 - k1*z2 + c*v1 + k1*z1 - m2*g)/m2
    return [dz1dt, dv1dt, dz2dt, dv2dt]

# Condiciones iniciales
z1_0 = 1*(-m1*g/k1 + k2/k1*1 - (k1+k2)/k1**2*m2*g + m2/k1 * g ) # posición inicial masa 1
v1_0 = 0.0  # velocidad inicial masa 1
z2_0 = 1*(-m1*g/k1 + k2/k1*1 - (k1+k2)/k1**2*m2*g) # posición inicial masa 2
v2_0 = 0.0  # velocidad inicial masa 2
x0 = [z1_0, v1_0, z2_0, v2_0]
t_span = (0, 100)  # intervalo de tiempo
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # puntos de tiempo para evaluar la solución
sol = solve_ivp(f, t_span, x0, t_eval=t_eval)
z1, v1, z2, v2 = sol.y
t = sol.t
# Graficar resultados
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, z1, label='Posición masa 1 (z1)')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(t, z2, label='Posición masa 2 (z2)')
plt.legend()
plt.show()