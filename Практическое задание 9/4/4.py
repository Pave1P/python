import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
indices = np.where(x[:-1] == 0)[0]
max_after_zero = np.max(x[indices + 1])

print("Максимальный элемент после нуля:", max_after_zero)