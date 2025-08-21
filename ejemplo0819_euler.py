# Autor: Carlos Juarez
# Fecha: 19/08/2025
# Descripcion: Ejemplo de euler y comparacion con analitica

import numpy as np
import matplotlib.pyplot as plt
# DAtos del sistema
M = 100 # Masa del sistema kg
B = 0.1 # Coeficiente de friccion kg/s
# Condiciones iniciales
v0 = 10 # Velocidad inicial m/s
# Tiempo de simulacion
t0 = 0 # s
tf = 5000 # s
N = 1000 # Numero de pasos
# Vector de tiempo
t = np.linspace(t0, tf, N+1)
# Vector de velocidad
v_analitica = v0 * np.exp(-B/M * t)
# graficando
plt.plot(t, v_analitica, label='Analitica', color='blue')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad del sistema con friccion')
plt.grid()
plt.legend()
plt.show()  
