with open('matrix.txt', 'r') as f:
    lines = f.readlines()

matrix = [[int(num) for num in line.strip().split(',')] for line in lines]

# Нахождение суммы всех элементов, максимального и минимального элементов
flat_matrix = [num for row in matrix for num in row]
matrix_sum = sum(flat_matrix)
max_element = max(flat_matrix)
min_element = min(flat_matrix)

print("Сумма всех элементов:", matrix_sum)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)