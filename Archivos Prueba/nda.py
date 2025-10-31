import control as ct
import numpy as np
import matplotlib.pyplot as plt

G = ct.tf(1,[0.1,1])
# Lugar de las raíces
respuesta = ct.root_locus_map(G) # G es la función de transferencia de lazo abierto
plt.figure()
respuesta.plot()
plt.show()