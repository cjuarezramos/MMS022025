import control as ct
import numpy as np
import matplotlib.pyplot as plt
K = 1
B = 0.1
J = 0.01
num_ol = [K]
den_ol = [J, B, 0]
G = ct.tf(num_ol, den_ol)
# respuesta al escalón del sistema de lazo abierto
# Lugar de las raíces del sistema
ct.root_locus_map(G).plot()
plt.show()