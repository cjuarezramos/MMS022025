import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# -------------------------------
# Parámetros del problema
# -------------------------------
L = 1.0            # Longitud de la barra (m)
nx = 50            # Número de nodos
dx = L / (nx - 1)  # Espaciado entre nodos
alpha = 0.01       # Difusividad térmica (m^2/s)
dt = 0.001         # Paso de tiempo (s)
nt = 200           # Número de pasos de tiempo

# -------------------------------
# Condiciones iniciales y frontera
# -------------------------------
T = np.zeros(nx)           # Temperatura inicial en todos los nodos
T[int(nx/2)] = 100         # Pico de temperatura en el centro
T[0] = 0                   # Extremo izquierdo
T[-1] = 0                  # Extremo derecho

# -------------------------------
# Factor de estabilidad
# -------------------------------
r = alpha * dt / dx**2
if r > 0.5:
    print(f"Advertencia: el método puede ser inestable (r = {r:.3f})")

# -------------------------------
# Configuración de la figura
# -------------------------------
fig, ax = plt.subplots()
x = np.linspace(0, L, nx)
line, = ax.plot(x, T, color='r', lw=2)
ax.set_xlim(0, L)
ax.set_ylim(0, 120)
ax.set_xlabel('Posición (m)')
ax.set_ylabel('Temperatura (°C)')
title = ax.set_title('Evolución de la temperatura en la barra')

# -------------------------------
# Función para actualizar la animación
# -------------------------------
def update(frame):
    global T
    T_new = T.copy()
    for i in range(1, nx-1):
        T_new[i] = T[i] + r * (T[i+1] - 2*T[i] + T[i-1])
    T[:] = T_new
    line.set_ydata(T)
    title.set_text(f'Evolución de la temperatura (t = {frame*dt:.3f} s)')
    return line, title

# -------------------------------
# Crear la animación
# -------------------------------
ani = animation.FuncAnimation(fig, update, frames=nt, interval=50, blit=True)

# Guardar la animación como archivo .mp4
ani.save('evolucion_temperatura.mp4', writer='ffmpeg')

# Mostrar la animación en pantalla
plt.show()