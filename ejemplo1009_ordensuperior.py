#Autor: Carlos Juárez
#Fecha: 10/09/2025  
# Descripción: Amortiguador de un carro- modelo 1/4 de un carro


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema
mc = 250  # masa del carro en kg
kc = 15000  # constante del resorte en N/m
cc = 1000  # coeficiente de amortiguamiento en Ns/m
mw = 30  # masa de la rueda en kg
kw = 200000  # constante del resorte de la rueda en N/m
cw = 1500  # coeficiente de amortiguamiento de la rueda en Ns/m
g = 9.81  # aceleración debido a la gravedad en m/s^2
yi = 0.0 # escalon de entrada
dyi = 0.0 # velocidad del escalon de entrada

# Función que define el sistema de ecuaciones diferenciales
def sistema(y, t):
    x1, x2, x3, x4 = y
    dx1dt = x2
    dx2dt = (-mc*g-kc*(x1-x3)-cc*(x2-x4)) / mc
    dx3dt = x4
    dx4dt = (kc*(x1-x3)+cc*(x2-x4)-kw*(x3-yi)-cw*(x4-dyi)-mw*g) / mw
    return [dx1dt, dx2dt, dx3dt, dx4dt]

# Condiciones iniciales
y0 = [0, 0, 0, 0]  # [x1, x1', x3, x3']
t = np.linspace(0, 5, 500)  # tiempo de simulación

# Resolver las ecuaciones diferenciales
sol = odeint(sistema, y0, t)

x1 = sol[:, 0]  # desplazamiento del carro
x3 = sol[:, 2]  # desplazamiento de la rueda

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label='Desplazamiento del carro (m)')
plt.plot(t, x3, label='Desplazamiento de la rueda (m)')
plt.title('Respuesta del sistema de amortiguador de un carro')
plt.xlabel('Tiempo (s)')
plt.ylabel('Desplazamiento (m)')
plt.legend()
plt.grid()
plt.show()

