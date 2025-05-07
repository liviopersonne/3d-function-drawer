import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


def plot_3d(z_formula, xg=-10, xd=10, yg=-10, yd=10):
    # Make data
    X = np.linspace(xg, xd, 1000)
    Y = np.linspace(yg, yd, 1000)
    X, Y = np.meshgrid(X, Y)
    Z = eval(z_formula.replace("x","X").replace("y","Y"))

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=True)
    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.01f}')
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)


    plt.show()



z_formula = input("z = ")
plot_3d(z_formula, -1, 1, -1, 1)