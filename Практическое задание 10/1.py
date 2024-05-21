import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Зададим x в диапазоне от -1 до 1
x = np.linspace(-1, 1, 400)

# Создадим фигуру и оси
plt.figure(figsize=(10, 6))

# Построим полиномы Лежандра от 1 до 7 степени
for n in range(1, 8):
    Pn = legendre(n)
    plt.plot(x, Pn(x), label=f'n = {n}')

# Заголовок и легенда
plt.title('Полиномы Лежандра')
plt.legend()
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.grid(True)

# Покажем график
plt.show()