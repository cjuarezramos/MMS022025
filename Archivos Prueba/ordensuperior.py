import numpy as np
import sympy as sp

# Definir las variables simbólicas
s = sp.symbols('s')
Bc = sp.symbols('Bc')  # Coeficiente de amortiguamiento del carro
Bw = sp.symbols('Bw')  # Coeficiente de amortiguamiento de la rueda
Kc = sp.symbols('Kc')  # Constante del resorte del carro    
Kw = sp.symbols('Kw')  # Constante del resorte de la rueda
Mc = sp.symbols('Mc')  # Masa del carro
Mw = sp.symbols('Mw')  # Masa de la rueda
R = sp.symbols('R')    # Entrada del sistema

# Definir las funciones de transferencia
X1 = sp.Function('X1')(s)  # Desplazamiento del carro
X3 = sp.Function('X3')(s)  # Desplazamiento de la
# Definir las ecuaciones del sistema
eq1 = sp.Eq(Mc*s**2*X1 + Bc*s*(X1 - X3) + Kc*(X1 - X3), 0)
eq2 = sp.Eq(Mw*s**2*X3 + Bw*s*(X3 - R) + Kw*(X3 - R) + Bc*s*(X3 - X1) + Kc*(X3 - X1), 0)
# Resolver el sistema de ecuaciones
sol = sp.solve((eq1, eq2), (X1, X3))    
# Obtener las funciones de transferencia
G1 = sp.simplify(sol[X1] / R)
G2 = sp.simplify(sol[X3] / R)   
# Mostrar las funciones de transferencia
sp.pprint(G1)
#sp.pprint(G2) 