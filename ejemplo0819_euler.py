# Autor: Carlos Juarez
# Fecha: 19/08/2025
# Descripcion: Ejemplo de euler y comparacion con analitica

import numpy as np
import matplotlib.pyplot as plt
# DAtos del sistema
M = 10 # Masa del sistema kg
B = 0.1 # Coeficiente de friccion kg/s
# Condiciones iniciales
v0 = 50 # Velocidad inicial m/s
# Tiempo de simulacion
t0 = 0 # s
tf = 500 # s
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
v_euler[0] = v0  # Condición inicial
# método de euler
for i in range(N):
    v_euler[i+1] = v_euler[i] + h * (-B/M * v_euler[i])
    print(v_euler)
#Gráficos
plt.plot(t, v_analitica, label='Analitica', color='blue')
plt.plot(t, v_euler, label='Euler', color='red')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad del sistema con friccion')
plt.grid()
plt.legend()
plt.show()  




