import control as ct
import numpy as np
from scipy.integrate import solve_ivp

# Función resolve euler
def f_euler(f, tspan, x0, h):
    class Solution:
        pass
    sol = Solution()

    t0, tf = tspan
    N = int((tf - t0) / h) + 1
    t = np.linspace(t0, tf, N)
    x = np.zeros((len(x0), N))
    x[:, 0] = x0
    for i in range(1, N):
        x[:, i] = x[:, i-1] + h * f(t[i-1], x[:, i-1])
    sol.t = t
    sol.y = x
    return sol


def f_odeint(x,t):
    dxdt = (1/K)*(-H*x)
    return dxdt
def f_solve_ivp(t, x):
    dxdt = (1/K)*(-H*x)
    return dxdt
x0 = 0.1
tsimu = 1
H = 0.01
K = 0.1
# Función de transferencia del sistema
num = [1]
den = [H, K]
G = ct.tf(num, den)
print(G)
print(G.poles())

sol3 = f_euler(f_solve_ivp, [0, tsimu], [x0], h=tsimu/10)

sol2 = solve_ivp(f_solve_ivp, [0, tsimu], [x0])

import matplotlib.pyplot as plt
plt.figure()

plt.plot(sol3.t, sol3.y[0])
plt.plot(sol2.t, sol2.y[0])

print(sol2)





# Parámetros del sistema

tau = 0.1  # Constante de tiempo

# Función de transferencia
G = ct.tf([1], [tau, 1])

# Lugar de las raíces
plt.figure()
rlist = ct.root_locus(G)


# Respuesta al escalón
# Función de transferencia de lazo cerrado
K = [0.5,1,10,100]  # Ganancia
plt.figure()
for k in K:
    T = ct.feedback(k*G, 1)
    t, y = ct.step_response(T)
    plt.plot(t, y)
plt.show()