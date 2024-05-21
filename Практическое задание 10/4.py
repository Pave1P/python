import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Создаем данные для графика
x = np.linspace(0, 10, 1000)

# Начальные параметры волн
initial_freq1 = 1
initial_amp1 = 1
initial_freq2 = 1
initial_amp2 = 1

# Функция для обновления графиков
def update(val):
    freq1 = sfreq1.val
    amp1 = samp1.val
    freq2 = sfreq2.val
    amp2 = samp2.val
    
    wave1.set_ydata(amp1 * np.sin(freq1 * x))
    wave2.set_ydata(amp2 * np.sin(freq2 * x))
    sum_wave.set_ydata(amp1 * np.sin(freq1 * x) + amp2 * np.sin(freq2 * x))
    fig.canvas.draw_idle()

# Создаем фигуру и оси для графиков
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)

# Создаем графики начальных волн и их суммы
wave1, = plt.plot(x, initial_amp1 * np.sin(initial_freq1 * x), label='Wave 1')
wave2, = plt.plot(x, initial_amp2 * np.sin(initial_freq2 * x), label='Wave 2')
sum_wave, = plt.plot(x, initial_amp1 * np.sin(initial_freq1 * x) + initial_amp2 * np.sin(initial_freq2 * x), label='Sum Wave')

# Настраиваем легенду и сетку
plt.legend()
plt.grid(True)

# Определяем цвет фона для слайдеров
axcolor = 'lightgoldenrodyellow'

# Создаем оси для слайдеров
axfreq1 = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor=axcolor)
axamp1 = plt.axes([0.1, 0.20, 0.65, 0.03], facecolor=axcolor)
axfreq2 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
axamp2 = plt.axes([0.1, 0.10, 0.65, 0.03], facecolor=axcolor)

# Создаем слайдеры
sfreq1 = Slider(axfreq1, 'Freq 1', 0.1, 10.0, valinit=initial_freq1)
samp1 = Slider(axamp1, 'Amp 1', 0.1, 10.0, valinit=initial_amp1)
sfreq2 = Slider(axfreq2, 'Freq 2', 0.1, 10.0, valinit=initial_freq2)
samp2 = Slider(axamp2, 'Amp 2', 0.1, 10.0, valinit=initial_amp2)

# Подключаем функцию обновления к изменениям значений слайдеров
sfreq1.on_changed(update)
samp1.on_changed(update)
sfreq2.on_changed(update)
samp2.on_changed(update)

# Показываем график
plt.show()
