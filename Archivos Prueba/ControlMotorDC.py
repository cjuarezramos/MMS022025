# Autor: Carlos Juárez
# Fecha: 2025-09-24
# Descripción: Control de un motor DC 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del motor DC
R = 2.0      # Resistencia (ohmios)
L = 0.5      # Inductancia (henrios)
Kb = 0.1     # Constante de fuerza contraelectromotriz (V·s/rad)
Kt = 0.1     # Constante de torque (N·m/A)
J = 0.01     # Momento de inercia del rotor (kg·m²)
b = 0.1      # Coeficiente de fricción viscosa (N·m·s/rad)
#V = 10.0     # Voltaje de entrada (V)
t_span = (0, 5)  # Intervalo de tiempo
t_eval = np.linspace(t_span[0], t_span[1], 1000)
# Condiciones iniciales 
i0 = 0.0  # Corriente inicial (A)
omega0 = 0.0  # Velocidad angular inicial (rad/s)
v20 = 0.0  # Variable de control inicial
x0 = [i0, omega0, v20]   
wref = 1.0  # Referencia de velocidad (rad/s)
def motor_dc(t, x):
    
    i = x[0]       # Corriente
    omega = x[1]   # Velocidad angular
    v2 = x[2]   # Variable de control
    
    e = wref - omega
    Kp = 10
    Ti = 0.07
    V = v2 + Kp * e 
    di_dt = (V - R*i - Kb*omega) / L
    domega_dt = (Kt*i - b*omega) / J
    dv2_dt = Kp/Ti * e
    return [di_dt, domega_dt, dv2_dt]
sol = solve_ivp(motor_dc, t_span, x0, t_eval=t_eval)
i, omega, v2 = sol.y
t = sol.t
# Graficar resultados
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(t, i, label='Corriente (A)')
plt.title('Respuesta del Motor DC - Corriente')
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(t, omega, label='Velocidad angular (rad/s)')
plt.plot(t, wref*np.ones_like(t), 'r--', label='Referencia Velocidad (rad/s)')
plt.title('Respuesta del Motor DC - Velocidad Angular')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad angular (rad/s)')
plt.legend()
plt.show()
