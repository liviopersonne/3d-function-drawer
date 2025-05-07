import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Constantes
pi = np.pi
a = 5e-4
b = 5e-4
lamb = 633e-9
D = 4
K = .005


# Make data.
X = np.arange(-.1, .1, 0.0001)
Y = np.arange(-.1, .1, 0.0001)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
I0 = K*np.exp(-R**2)
Z = 4*I0*(1 + np.cos(2*pi*X*a / (lamb*D)))*(1 + np.cos(2*pi*Y*b / (lamb*D)))





# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()