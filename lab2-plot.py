import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_int

x = get_int("X: ")

x_knots = np.linspace(0, x*np.pi, 201)
y_knots = np.linspace(0, x*np.pi, 201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(2**X+3*Y)
Z = np.cos(3*R)*np.cos(R)
ax = Axes3D(plt.figure(figsize=(6,5)))
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
print("trwa rysowanie...")
plt.show()