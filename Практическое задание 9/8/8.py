import numpy as np

array = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
nonzero_indices = np.nonzero(array)

print("Индексы ненулевых элементов:", nonzero_indices)