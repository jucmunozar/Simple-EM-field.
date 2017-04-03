import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


v1 = np.array([[0, 0, 0, -1, 0, 0]]) 
v2 =  np.array([[0, 0, 0, 0, 1, 0]])
v3 = np.array([[0, 0, 0, 0, 0, 1]]) 

X1, Y1, Z1, U1, V1, W1 = zip(*v1)
X2, Y2, Z2, U2, V2, W2 = zip(*v2)
X3, Y3, Z3, U3, V3, W3 = zip(*v3)
theta = np.linspace(- 4.0 * np.pi, 4.0 * np.pi, num = 1000)
z = np.linspace(0, 4, num = 1000)
x =  np.sin(theta)
y =  np.cos(theta)
ax.plot(x, y, z, label='Movimiento de partícula cargada bajo efecto de campo EM', color = 'g')
ax.quiver(X1, Y1, Z1, U1, V1, W1,pivot='tail',length=1,arrow_length_ratio=0.3, color = 'y', label = 'Campo Magnético')
ax.quiver(X2, Y2, Z2, U2, V2, W2, pivot='tail',length=1,arrow_length_ratio=0.3, color = 'b', label = 'Campo Eléctrico')
ax.quiver(X3, Y3, Z3, U3, V3, W3, pivot='tail',length=2,arrow_length_ratio=0.2, color = 'g', label = 'Dirección del Movimiento')

ax.legend()
plt.show()

