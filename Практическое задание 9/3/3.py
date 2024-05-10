import numpy as np

random_array = np.random.normal(size=(10, 4))

min_v = np.min(random_array, axis=0)
max_v = np.max(random_array, axis=0)
mean_v = np.mean(random_array, axis=0)
std_deviation = np.std(random_array, axis=0)

first_five_rows = random_array[:5]

print("Минимальные значения по столбцам:", min_v)
print("Максимальные значения по столбцам:", max_v)
print("Средние значения по столбцам:", mean_v)
print("Стандартное отклонение по столбцам:", std_deviation)