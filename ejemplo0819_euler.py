# Autor: Carlos Juarez
# Fecha: 19/08/2025
# Descripcion: Ejemplo de euler y comparacion con analitica

import numpy as np
import matplotlib.pyplot as plt
# DAtos del sistema
M = 10 # Masa del sistema kg
B = 0.1 # Coeficiente de friccion kg/s
# Condiciones iniciales
v0 = 0 # Velocidad inicial m/s
# Tiempo de simulacion
t0 = 0 # s
tf = 1000 # s
N = 10 # Numero de intervalos
# Vector de tiempo
t = np.linspace(t0, tf, N+1)
# Vector de velocidad
v_analitica = v0 * np.exp(-B/M * t)
'''# graficando
plt.plot(t, v_analitica, label='Analitica', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad del sistema con friccion')
plt.grid()
plt.legend()
plt.show()  
'''
# Solución por métodos numéricos
# Paso de tiempo
h = (tf - t0) / N
# Inicializando arreglos para almacenar la solución
v_euler = np.zeros(N+1)
v_euler[0] =  v0  # Condición inicial
# método de eulerd
for i in range(N):
    v_euler[i+1] = v_euler[i] + h * (-B/M * v_euler[i])
    #print(v_euler)

# Método de Heun
v_heun = np.zeros(N+1)
v_heun[0] = v0
# dv/dt = -B/M*v
def f(v):
    return -B/M*v + 1

for i in range(N):
    vtemp = v_heun[i] + h*f(v_heun[i])
    v_heun[i+1] = v_heun[i] + h*(f(v_heun[i])+f(vtemp))/2
    print(v_heun)
# Metódo RK2/3
v_rk23 = np.zeros(N+1)
v_rk23[0] = v0
for i in range(N):
    k1 = f(v_rk23[i])
    vtemp = v_rk23[i] + 3/4*k1*h
    k2 = f(vtemp)
    v_rk23[i+1] = v_rk23[i] + h*(1/3*k1+2/3*k2)

# Método RK4
v_rk4 = np.zeros(N+1)
v_rk4[0] = v0
for i in range(N):
    k1 = f(v_rk4[i])
    vtemp = v_rk4[i]+1/2*h*k1
    k2 = f(vtemp)
    vtemp = v_rk4[i] + 1/2*h*k2
    k3 = f(vtemp)
    vtemp = v_rk4[i] + h*k3
    k4 = f(vtemp)
    v_rk4[i+1] = v_rk4[i] + h * (k1+2*k2+2*k3+k4)/6





#Gráficos
plt.plot(t, v_analitica, label='Analitica', color='blue')
plt.plot(t, v_euler, label='Euler', color='red')
plt.plot(t, v_heun, label='Heun', color='black')
plt.plot(t, v_rk23, label='RK23', color='green')
plt.plot(t, v_rk4, label='RK4', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad del sistema con friccion')
plt.grid()
plt.legend()
plt.show()  




