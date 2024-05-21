import numpy as np
import matplotlib.pyplot as plt

# Создадим фигуру и оси
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Соотношения частот
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

t = np.linspace(0, 2 * np.pi, 1000)

for ax, (a, b) in zip(axs.flatten(), ratios):
    x = np.sin(a * t)
    y = np.sin(b * t)
    ax.plot(x, y)
    ax.set_title(f'Lissajous Figure: {a}:{b}')
    ax.grid(True)

plt.tight_layout()
plt.show()