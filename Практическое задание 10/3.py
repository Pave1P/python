import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры фигуры Лиссажу
A, B = 5, 4  # Частоты
delta = 0  # Сдвиг фаз

t = np.linspace(0, 2 * np.pi, 1000)

# Создадим фигуру и оси
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Установим границы осей
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Обновление графика для каждого кадра
def update(freq):
    x = np.sin(A * t + delta)
    y = np.sin(freq * t)
    line.set_data(x, y)
    return line,

# Создание анимации
ani = FuncAnimation(fig, update, frames=np.linspace(1, 2, 200), blit=True)

# Покажем анимацию
plt.title('Lissajous Figure Animation')
plt.show()