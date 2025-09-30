# Autor: Carlos Juarez
# Fecha: 2025-09-30
# Descripción: Control de un motor DC usando el método de Euler
import numpy as np
import matplotlib.pyplot as plt
# Parámetros del motor DC
R = 2.27
L = 0.0047
Ka = 0.25
Km = 0.25
J = 0.00246
B = 0.003026   # Constante de fuerza contraelectromotriz (V·s/rad)