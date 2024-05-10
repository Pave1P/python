import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species_column = iris[:, 4]
unique_species, counts = np.unique(species_column, return_counts=True)

print("Уникальные значения:", unique_species)
print("Количество каждого уникального значения:", counts)