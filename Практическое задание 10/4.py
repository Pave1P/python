import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создадим начальные параметры волн
freq1 = 1
amp1 = 1
freq2 = 1
amp2 = 1

x = np.linspace(0, 10, 1000)

# Создадим фигуру и оси
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Исходные линии волн и их сумма
wave1, = plt.plot(x, amp1 * np.sin(freq1 * x), label='Wave 1')
wave2, = plt.plot(x, amp2 * np.sin(freq2 * x), label='Wave 2')
sum_wave, = plt.plot(x, amp1 * np.sin(freq1 * x) + amp2 * np.sin(freq2 * x), label='Sum Wave')

plt.legend()
plt.grid(True)

# Добавим слайдеры
axfreq1 = plt