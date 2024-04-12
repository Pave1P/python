# Читаем числа из файла и помещаем их в список
with open('input.txt', 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file]

# Сортируем числа по возрастанию цифр
sorted_numbers = sorted(numbers, key=lambda x: sorted(str(x)))

# Записываем отсортированные числа в файл
with open('output.txt', 'w') as output_file:
    for number in sorted_numbers:
        output_file.write(str(number) + '\n')