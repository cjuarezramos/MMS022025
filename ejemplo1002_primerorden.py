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
    tau = float(tau_entry.get())         # Constante de tiempo τ
    h = float(h_entry.get())             # Paso de integración h
    u = float(u_entry.get())             # Valor de entrada (escalón)
    
    t_max = float(t_entry.get())                           # Tiempo total de simulación (segundos)
    steps = int(t_max / h)               # Número de pasos de simulación
    t = np.linspace(0, t_max, steps)     # Vector de tiempo
    y = np.zeros(steps)                  # Inicializamos la salida y(t)

    # Aplicamos el método de Euler para resolver la ecuación diferencial
    for k in range(steps - 1):
        y[k+1] = y[k] + h * (-y[k] + u) / tau

    # Limpiamos el gráfico anterior
    ax.clear()
    # Graficamos la nueva respuesta
    ax.plot(t, y, label=f"τ={tau}, h={h}, u={u}")
    ax.set_title("Respuesta del sistema de primer orden")
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Salida y(t)")
    ax.grid(True)
    ax.legend()
    # Actualizamos el gráfico en la interfaz
    canvas.draw()

def reset():
    tau_entry.delete(0, tk.END)
    tau_entry.insert(0, "1.0")
    h_entry.delete(0, tk.END)
    h_entry.insert(0, "0.1")
    u_entry.delete(0, tk.END)
    u_entry.insert(0, "1.0")
    R_entry.delete(0, tk.END)
    R_entry.insert(0, "1000.0")
    C_entry.delete(0, tk.END)
    C_entry.insert(0, "1000.0")
    t_entry.delete(0, tk.END)
    t_entry.insert(0, "5.0")
    ax.clear()
    canvas.draw()

def actualizar_tau(*args):
    tau = float(tau_entry.get())
    C = float(C_entry.get())*1e-6
    if C != 0: 
        R = tau / C
        R_entry.delete(0, tk.END)
        R_entry.insert(0, str(round(R, 10)))
        t_entry.delete(0, tk.END)
        tsim = tau * 5
        t_entry.insert(0, str(round(tsim, 10)))

def actualizar_R(*args):
    R = float(R_entry.get())
    C = float(C_entry.get())*1e-6
    if C != 0: 
        tau = R * C
        tau_entry.delete(0, tk.END)
        tau_entry.insert(0, str(round(tau, 10)))
        t_entry.delete(0, tk.END)
        tsim = tau * 5
        t_entry.insert(0, str(round(tsim, 10)))
def actualizar_C(*args):
    C = float(C_entry.get())*1e-6
    R = float(R_entry.get())
    if C != 0: 
        tau = R * C
        tau_entry.delete(0, tk.END)
        tau_entry.insert(0, str(round(tau, 10)))
        t_entry.delete(0, tk.END)
        tsim = tau * 5
        t_entry.insert(0, str(round(tsim, 10)))

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Simulador de Sistema de Primer Orden")

# Creamos un contenedor para los controles
frame = ttk.Frame(root, padding="10")
frame.grid()



# Etiquetas y campos de entrada para τ, h y u

ttk.Label(frame, text="Datos del Sistema", font=("Arial", 14)).grid(row=0, column=[0], columnspan=2)

ttk.Label(frame, text="R (Ω):").grid(column=0, row=1)
R_entry = ttk.Entry(frame)
R_entry.insert(0, "1000.0")               # Valor inicial por defecto
R_entry.grid(column=1, row=1)

ttk.Label(frame, text="C (μF):").grid(column=0, row=2)
C_entry = ttk.Entry(frame)
C_entry.insert(0, "1000.0")               # Valor inicial por defecto
C_entry.grid(column=1, row=2)

Tau = float(R_entry.get()) * float(C_entry.get())*1e-6  # Constante de tiempo τ = R*C

ttk.Label(frame, text="Tau (τ):").grid(column=0, row=3)
tau_entry = ttk.Entry(frame)
tau_entry.insert(0, str(round(Tau, 10)))               # Valor inicial por defecto
tau_entry.grid(column=1, row=3)

ttk.Label(frame, text="Datos de Simulación", font=("Arial", 14)).grid(row=0, column=[3], columnspan=2)
ttk.Label(frame, text="Paso h (s):").grid(column=3, row=1)
h_entry = ttk.Entry(frame)
h_entry.insert(0, "0.1")                 # Valor inicial por defecto
h_entry.grid(column=4, row=1)

ttk.Label(frame, text="Tiempo de simulación (s):").grid(column=3, row=2)
t_entry = ttk.Entry(frame)
tsim = Tau * 5
t_entry.insert(0, str(round(tsim, 10)))                 # Valor inicial por defecto
t_entry.grid(column=4, row=2)


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
fig, ax = plt.subplots(figsize=(8, 4))   # Creamos la figura y el eje
canvas = FigureCanvasTkAgg(fig, master=root)  # Integramos el gráfico en Tkinter
canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)


# Datos actualizados automáticamente
tau_entry.bind("<KeyRelease>", actualizar_tau)
R_entry.bind("<KeyRelease>", actualizar_R)
C_entry.bind("<KeyRelease>", actualizar_C)

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

