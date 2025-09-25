# codigo para resolver pendulo

# Modulos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# parametros del sistema
B = 0.5
L = 1
M = 1
g = 9.81
u = M*g*L

#funcion NO LINEAL
def f(x,t):
    theta = x[0]
    omega = x[1]
    dtheta_dt = omega
    domega_dt = -B/M*omega - g/L *np.sin(theta) + u*.9/L**2/M
    return [dtheta_dt,domega_dt]

# funcion LINEAL (aproximacion para angulos pequeños)
def f_lineal(x,t):
    theta = x[0]
    omega = x[1]
    dtheta_dt = omega
    domega_dt = -B/M*omega - g/L*theta + u/M/L**2
    return [dtheta_dt,domega_dt]

theta0_90 = 0
omega0_90 = 0
u90 = 0
# funcion LINEAL (aproximacion para angulo 90 grados)
def f_lineal_90(x,t):
    theta = x[0]
    omega = x[1]
    dtheta_dt = omega
    domega_dt = -B/M*omega - 0.1/M/L**2
    return [dtheta_dt,domega_dt]

# tiempo
tfin = 25
t = np.linspace(0,tfin,500)
# condiciones iniciales
theta0 = np.pi/2 
omega0 = 0 

sol = odeint(f,[theta0,omega0],t)
sol_lineal = odeint(f_lineal, [theta0,omega0], t)
sol_lineal_90 = odeint(f_lineal_90, [theta0_90,omega0_90], t)

plt.plot(t,sol[:,0])
plt.plot(t,sol_lineal[:,0])
plt.show()
plt.figure()
plt.plot(t,sol_lineal_90[:,0])
plt.show()
