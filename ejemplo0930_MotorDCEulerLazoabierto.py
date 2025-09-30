#Autor: Carlos Juarez
#Fecha: 30/09/2025
#Descripcion: Simulacion de un motor DC con Euler en lazo abierto

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
R = 2.27 # Resistencia (Ohm)
L = 0.0047 # Inductancia (H)
Ka = 0.25   # Constante de ganancia del amplificador (V/rad/s)
Km = 0.25   # Constante de ganancia del motor (V/rad/s)
J = 0.00246 # Inercia del rotor (kg*m^2)
B = 0.003026 # Coeficiente de fricción viscosa (N*m*s/rad)

## Ejemplo Lazo Abierto
# Función a resolver
def motordc(t,x):
    i = x[0]  # Corriente (A)
    w = x[1]  # Velocidad angular (rad/s)
    V = voltaje(t)  # Voltaje de entrada (V)
    TL = carga(t)  # Torque de carga (N*m)
    di_dt = -R/L*i - Ka/L*w + V/L
    dw_dt = -B/J*w + Km/J*i - TL/J
    
    return np.array([di_dt, dw_dt])
def voltaje(t):
    if t < 0.5:
        return 0
    else:
        return 11  # Voltaje constante de 12V después de 0.5 segundos
def carga(t):
    if t < 2:
        return 0
    else:
        return 0.2  # Torque de carga constante de 0.2 N*m después de 2 segundos
    
# Datos de simulación
h = 1e-4  # Paso de tiempo (s)
tf = 1    # Tiempo final (s)
t = np.arange(0, tf, h)  # Vector de tiempo
n = len(t)  # Número de pasos de tiempo 

# Inicialización de variables
i1 = np.zeros(n)  # Vector de corriente
w1 = np.zeros(n)  # Vector de velocidad angular

# Condiciones iniciales
i1[0] = 0  # Corriente inicial (A)
w1[0] = 0  # Velocidad angular inicial (rad/s)

# Método de Euler
for k in range(n-1):
    xk = np.array([i1[k], w1[k]])
    xk1 = xk + h * motordc(t[k], xk)
    i1[k+1] = xk1[0]
    w1[k+1] = xk1[1]   

'''# Graficas
plt.figure()
plt.plot(t, i1, label='Corriente (A)')
plt.title('Corriente del motor DC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.grid()
plt.legend()
plt.show() 
plt.figure()
plt.plot(t, w1, label='Velocidad (rad/s)', color='orange')
plt.title('Velocidad del motor DC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (rad/s)')
plt.grid()
plt.legend()
plt.show()
'''
# Lazo cerrado - Control Proporcional
Kp = 1  # Ganancia proporcional
# Función de referencia
def referencia(t):
    if t < 0.5:
        return 0
    else:
        return 40  # Referencia constante de 40 rad/s después de 0.5 segundos

# Función a resolver con control proporcional
def motordc_control(t,x):
    i = x[0]  # Corriente (A)
    w = x[1]  # Velocidad angular (rad/s)
    w_ref = referencia(t)  # Referencia de velocidad (rad/s)
    error = w_ref - w  # Error de velocidad
    V = Kp * error  # Control proporcional
    TL = 0 #carga(t)  # Torque de carga (N*m)
    di_dt = -R/L*i - Ka/L*w + V/L
    dw_dt = -B/J*w + Km/J*i - TL/J
    
    return np.array([di_dt, dw_dt])
# Soluciòn con euler
i2 = np.zeros(n)  # Vector de corriente
w2 = np.zeros(n)  # Vector de velocidad angular
# Condiciones iniciales
i2[0] = 0  # Corriente inicial (A)
w2[0] = 0  # Velocidad angular inicial (rad/s)
# Método de Euler
for k in range(n-1):
    xk = np.array([i2[k], w2[k]])
    xk1 = xk + h * motordc_control(t[k], xk)
    i2[k+1] = xk1[0]
    w2[k+1] = xk1[1]

# Graficas
'''
plt.figure()
plt.plot(t, i1, label = 'Corriente(A) Lazo Abierto')
plt.plot(t, i2, label='Corriente (A) Lazo Cerrado', color='orange')
plt.title('Corriente del motor DC con Control Proporcional')
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.grid()
plt.legend()
plt.show()
'''
'''
plt.figure()
wref = np.array([referencia(ti) for ti in t])
plt.plot(t, wref, label='Referencia (rad/s)', linestyle='--', color='green')
plt.plot(t, w1, label = 'Velocidad(rad/s) Lazo Abierto')
plt.plot(t, w2, label='Velocidad (rad/s) Lazo Cerrado', color='orange')
plt.title('Velocidad del motor DC con Control Proporcional')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (rad/s)')
plt.grid()
plt.legend()
plt.show()
'''
# Control Proporcional Integral
Kp = 1  # Ganancia proporcional
Ti = 0.1  # Constante de tiempo integral
# Función a resolver con control proporcional integral
def motordc_control_pi(t,x):
    i = x[0]  # Corriente (A)
    w = x[1]  # Velocidad angular (rad/s)
    v2 = x[2]  # Accion integral
    w_ref = referencia(t)  # Referencia de velocidad (rad/s)
    error = w_ref - w  # Error de velocidad
    V = Kp * error + v2  # Control proporcional integral
    TL = 0 #carga(t)  # Torque de carga (N*m)
    di_dt = -R/L*i - Ka/L*w + V/L
    dw_dt = -B/J*w + Km/J*i - TL/J
    dv2_dt = Kp/Ti * error  # Ecuación del integrador

    return np.array([di_dt, dw_dt, dv2_dt])
# Soluciòn con euler
i3 = np.zeros(n)  # Vector de corriente
w3 = np.zeros(n)  # Vector de velocidad angular
v3 = np.zeros(n)  # Vector de accion integral
# Condiciones iniciales
i3[0] = 0  # Corriente inicial (A)
w3[0] = 0  # Velocidad angular inicial (rad/s)
v3[0] = 0  # Accion integral inicial
# Método de Euler
for k in range(n-1):
    xk = np.array([i3[k], w3[k], v3[k]])
    xk1 = xk + h * motordc_control_pi(t[k], xk)
    i3[k+1] = xk1[0]
    w3[k+1] = xk1[1]
    v3[k+1] = xk1[2]
# Graficas
plt.figure()
wref = np.array([referencia(ti) for ti in t])
plt.plot(t, wref, label='Referencia (rad/s)', linestyle='--', color='green')
plt.plot(t, w1, label = 'Velocidad(rad/s) Lazo Abierto')
plt.plot(t, w2, label='Velocidad (rad/s) Lazo Cerrado P', color='orange')
plt.plot(t, w3, label='Velocidad (rad/s) Lazo Cerrado PI', color='red')
plt.title('Velocidad del motor DC con Control Proporcional e Integral')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (rad/s)')
plt.grid() 
plt.legend()
plt.show()
