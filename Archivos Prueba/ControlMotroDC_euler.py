# Autor: Carlos Juarez
# Fecha: 2025-09-30
# Descripción: Control de un motor DC usando el método de Euler
import numpy as np
import matplotlib.pyplot as plt
# Parámetros del motor DC
R = 2.27 # Resistencia del motor (ohmios)
L = 0.0047 # Inductancia del motor (henrios)
Ka = 0.25 # Constante de ganancia del motor (V·s/rad)
Km = 0.25 # Constante de torque del motor (N·m/A)
J = 0.00246 # Inercia del rotor (kg·m²)
B = 0.003026 # Constante de fricción viscosa (V·s/rad)

# Controlador:
Kp = 2 # Ganancia proporcional
Ti = 0.1 # Tiempo integral (s)

# Función para calcular la derivada del estado
def motor_dc_derivada(x, wref, Td):
    i = x[0] # Corriente del motor
    w = x[1] # Velocidad angular del motor
    u2 = x[2] # Variable para la integral del error (no se usa en este ejemplo)
    # Controlador proporcional
    error = wref - w
    u1 = Kp * error # acción proporcional
    u = u1 + u2 # Señal de control total
    # Ecuaciones diferenciales del motor DC
    di_dt = (u - R*i - Ka*w) / L
    dw_dt = (Km*i - B*w - Td) / J
    #ecuacion diferencial de la integral del error
    du2_dt = error * Kp/ Ti
    return np.array([di_dt, dw_dt, du2_dt])

# Método de Euler para resolver las ecuaciones diferenciales
def euler(motor_dc_derivada, x0, wref, t):
    dt = t[1] - t[0]
    x = np.zeros((len(t), len(x0)))
    x[0] = x0
    for k in range(1, len(t)):
        x[k] = x[k-1] + motor_dc_derivada(x[k-1], wref, Td[k-1]) * dt
    return x   
# Tiempo de simulación
tfin = 2
dt = 0.001
t = np.arange(0, tfin, dt)
# Condiciones iniciales
i0 = 0 # Corriente inicial
w0 = 0 # Velocidad angular inicial
u2_0 = 0 # Integral del error inicial
x0 = np.array([i0, w0, u2_0])
# Entrada de voltaje (escalón)
# u = np.ones(len(t)) * 12 # Voltaje constante de 12V
# Torque de carga (escalon)
Td = np.zeros(len(t))
Td[int(len(t)/2):] = 0.1 # Aplica un torque de

wref = 40 #rad/s 


# Simulación del motor DC
sol = euler(motor_dc_derivada, x0, wref, t)
# Graficar resultados
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, sol[:, 0], label='Corriente (A)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.title('Respuesta del Motor DC - Corriente')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(t, sol[:, 1], label='Velocidad Angular (rad/s)', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Angular (rad/s)')
plt.title('Respuesta del Motor DC - Velocidad Angular')
plt.grid()
plt.tight_layout()
plt.show()
# Fin del código