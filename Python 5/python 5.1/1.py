with open('input.txt', 'r') as input_file:
    # Читаем строку с числами и разбиваем её на отдельные числа
    numbers = input_file.readline().split()

    # Преобразуем числа из строкового формата в тип int
    numbers = [int(num) for num in numbers]

    # Вычисляем произведение чисел
    product = 1
    for num in numbers:
        product *= num

# Открываем файл для записи
with open('output.txt', 'w') as output_file:
    # Записываем произведение в файл
    output_file.write(str(product))