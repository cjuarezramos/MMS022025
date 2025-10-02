#Autor: Carlos Juárez
#Fecha: 2025-10-02
#Descripción: Ejemplo de un sistema de primer orden
# Se ha empleado copilot para la creación de este código

# Importamos las librerías necesarias
import tkinter as tk                      # Para crear la interfaz gráfica
from tkinter import ttk                  # Para usar widgets más modernos de Tkinter
import matplotlib.pyplot as plt          # Para graficar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Para integrar matplotlib en Tkinter
import numpy as np                       # Para cálculos numéricos y manejo de arrays




# Función que realiza la simulación del sistema de primer orden
def simulate():
    # Obtener los valores ingresados por el usuario desde la interfaz
    Z = float(Z_entry.get())         # Constante de tiempo τ
    wn = float(wn_entry.get())             # Paso de integración h
    h = float(h_entry.get())             # Paso de integración h
    u = float(u_entry.get())             # Valor de entrada (escalón)
    
    t_max = float(t_entry.get())                           # Tiempo total de simulación (segundos)
    steps = int(t_max / h)               # Número de pasos de simulación
    t = np.linspace(0, t_max, steps)     # Vector de tiempo
    y = np.zeros((steps, 2))                  # Inicializamos la salida y(t)

    # Aplicamos el método de Euler para resolver la ecuación diferencial
    for k in range(steps - 1):
        y[k+1, 0] = y[k, 0] + h * y[k, 1]
        y[k+1, 1] = y[k, 1] + h * ( -2*Z*wn*y[k, 1] - wn**2*y[k, 0] + wn**2*u )

    # Limpiamos el gráfico anterior
    ax.clear()
    # Graficamos la nueva respuesta
    ax.plot(t, y, label=f"wn={wn}, Z={Z}, u={u}")
    ax.set_title("Respuesta del sistema de segundo orden")
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Salida y(t)")
    ax.grid(True)
    ax.legend()
    # Actualizamos el gráfico en la interfaz
    canvas.draw()

def reset():
    B_entry.delete(0, tk.END)
    B_entry.insert(0, "1.0")
    h_entry.delete(0, tk.END)
    h_entry.insert(0, "0.1")
    u_entry.delete(0, tk.END)
    u_entry.insert(0, "1.0")
    J_entry.delete(0, tk.END)
    J_entry.insert(0, "1.0")
    K_entry.delete(0, tk.END)
    K_entry.insert(0, "1.0")
    t_entry.delete(0, tk.END)
    t_entry.insert(0, "5.0")
    wn_entry.delete(0, tk.END)
    wn_entry.insert(0, "1.0")
    Z_entry.delete(0, tk.END)
    Z_entry.insert(0, "1.0")
    ax.clear()
    canvas.draw()

def actualizar_wn(*args):
    wn = float(wn_entry.get())
    B = float(B_entry.get())
    K = float(K_entry.get())
    J = float(J_entry.get())

    if J != 0: 
        K = wn**2 * J
        K_entry.delete(0, tk.END)
        K_entry.insert(0, str(round(K, 10)))
        tiempo_simulacion()
        polos_sistema()

def actualizar_Z(*args):
    Z = float(Z_entry.get())
    K = float(K_entry.get())
    J = float(J_entry.get())
    if K != 0 and J != 0: 
        B = 2 * Z * np.sqrt(K*J)
        B_entry.delete(0, tk.END)
        B_entry.insert(0, str(round(B, 10)))
        tiempo_simulacion()
        polos_sistema()

def actualizar_B(*args):
    K = float(K_entry.get())
    B = float(B_entry.get())
    J = float(J_entry.get())
    Z = B / (2 * np.sqrt(K*J))
    Z_entry.delete(0, tk.END)
    Z_entry.insert(0, str(round(Z, 10)))
    tiempo_simulacion()
    polos_sistema()

def actualizar_J(*args):
    K = float(K_entry.get())
    B = float(B_entry.get())
    J = float(J_entry.get())
    Z = B / (2 * np.sqrt(K*J))
    Z_entry.delete(0, tk.END)
    Z_entry.insert(0, str(round(Z, 10)))
    wn = np.sqrt(K/J)
    wn_entry.delete(0, tk.END)
    wn_entry.insert(0, str(round(wn, 10)))
    tiempo_simulacion()
    polos_sistema()

def actualizar_K(*args):
    K = float(K_entry.get())
    B = float(B_entry.get())
    J = float(J_entry.get())
    if J != 0: 
        wn = np.sqrt(K/J)
        wn_entry.delete(0, tk.END)
        wn_entry.insert(0, str(round(wn, 10)))
        Z = B / (2 * np.sqrt(K*J))
        Z_entry.delete(0, tk.END)
        Z_entry.insert(0, str(round(Z, 10)))
        tiempo_simulacion()
        polos_sistema()

def tiempo_simulacion (*args):
    Z = float(Z_entry.get())
    wn = float(wn_entry.get())
    polo = -Z*wn + wn*(Z**2 - 1)**(1/2) 
    if np.imag(polo) != 0:
        tsim = 5 / (Z * wn)
    else:
        tsim = 5 * (1 / abs(polo))
    t_entry.delete(0, tk.END)
    t_entry.insert(0, str(round(tsim, 10)))

def polos_sistema(*args):
    Z = float(Z_entry.get())
    wn = float(wn_entry.get())
    polo1 = -Z*wn + wn*(Z**2 - 1)**(1/2)
    polo2 = -Z*wn - wn*(Z**2 - 1)**(1/2)
    polos_entry.delete(0, tk.END)
    polos_entry.insert(0, f"{round(np.real(polo1), 2)}+j{round(np.imag(polo1), 2)}, {round(np.real(polo2), 2)}+j{round(np.imag(polo2), 2)}")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Simulador de Sistema de Segundo Orden")

# Creamos un contenedor para los controles
frame = ttk.Frame(root, padding="15")
frame.grid()



# Etiquetas y campos de entrada para τ, h y u

ttk.Label(frame, text="Datos del Sistema", font=("Arial", 14)).grid(row=0, column=[0], columnspan=4)

ttk.Label(frame, text="J (kg.m2):").grid(column=0, row=1)
J_entry = ttk.Entry(frame)
J_entry.insert(0, "1.0")               # Valor inicial por defecto
J_entry.grid(column=1, row=1)

ttk.Label(frame, text="B (kg.s-1):").grid(column=0, row=2)
B_entry = ttk.Entry(frame)
B_entry.insert(0, "1.0")               # Valor inicial por defecto
B_entry.grid(column=1, row=2)

ttk.Label(frame, text="K (N.m/rad):").grid(column=0, row=3)
K_entry = ttk.Entry(frame)
K_entry.insert(0, "1.0")               # Valor inicial por defecto
K_entry.grid(column=1, row=3)

wn = float(np.sqrt(float(K_entry.get())/float(J_entry.get())))  # Frecuencia natural wn = sqrt(J/B)
Z = float(float(B_entry.get()) / (2 * np.sqrt(float(K_entry.get())*float(J_entry.get()))))  # Factor de amortiguamiento Z = B/(2*sqrt(K*J))

ttk.Label(frame, text="wn (rad/s):").grid(column=2, row=1)
wn_entry = ttk.Entry(frame)
wn_entry.insert(0, str(round(wn, 10)))               # Valor inicial por defecto
wn_entry.grid(column=3, row=1)

ttk.Label(frame, text="Z:").grid(column=2, row=2)
Z_entry = ttk.Entry(frame)
Z_entry.insert(0, str(round(Z, 10)))               # Valor inicial por defecto
Z_entry.grid(column=3, row=2)

ttk.Label(frame, text="Polos:").grid(column=2, row=3)
polos_entry = ttk.Entry(frame)
polos_sistema()
polos_entry.grid(column=3, row=3)



ttk.Label(frame, text="Datos de Simulación", font=("Arial", 14)).grid(row=0, column=[4], columnspan=2)
ttk.Label(frame, text="Paso h (s):").grid(column=4, row=1)
h_entry = ttk.Entry(frame)
h_entry.insert(0, "0.1")                 # Valor inicial por defecto
h_entry.grid(column=5, row=1)

ttk.Label(frame, text="Tiempo de simulación (s):").grid(column=4, row=2)
t_entry = ttk.Entry(frame)
tiempo_simulacion()
t_entry.grid(column=5, row=2)


ttk.Label(frame, text="Datos de Entrada", font=("Arial", 14)).grid(row=0, column=[6], columnspan=2)
ttk.Label(frame, text="Entrada u:").grid(column=6, row=1)
u_entry = ttk.Entry(frame)
u_entry.insert(0, "1.0")                 # Valor inicial por defecto
u_entry.grid(column=7, row=1)




# Botón para ejecutar la simulación
ttk.Button(frame, text="Simular", command=simulate).grid(column=2, row=4, columnspan=2)
# Botón para resetear los campos y el gráfico
ttk.Button(frame, text="Resetear", command=reset).grid(column=5, row=4, columnspan=2)

# Configuración del gráfico con matplotlib
fig, ax = plt.subplots(figsize=(16, 9))   # Creamos la figura y el eje
canvas = FigureCanvasTkAgg(fig, master=root)  # Integramos el gráfico en Tkinter
canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)


# Datos actualizados automáticamente
wn_entry.bind("<KeyRelease>", actualizar_wn)
B_entry.bind("<KeyRelease>", actualizar_B)
J_entry.bind("<KeyRelease>", actualizar_J)
Z_entry.bind("<KeyRelease>", actualizar_Z)
K_entry.bind("<KeyRelease>", actualizar_K)

def on_click(event):
    if event.inaxes:
        x = event.xdata
        y = event.ydata
        ax.plot(x, y, 'ro')  # Marca el punto
        ax.text(x, y, f'({x:.2f}, {y:.2f})', fontsize=9, color='red')
        canvas.draw()

canvas.mpl_connect("button_press_event", on_click)

# Ejecutamos el bucle principal de la interfaz
root.mainloop()

