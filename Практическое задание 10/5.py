import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создадим данные для MSE
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)
Z = (X - 2)**2 + (Y - 3)**2

# Создадим фигуру и оси для двух графиков
fig = plt.figure(figsize=(14, 6))

# Первый график
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# Второй график с логарифмической осью Z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zscale('log')
ax2.set_title('MSE (Log Scale)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(Z)')

plt.show()