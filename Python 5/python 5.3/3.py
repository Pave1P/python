# Открываем файл и читаем данные с указанием кодировки
with open('дети.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Инициализируем переменные для хранения информации о самом старшем и младшем ребенке
max_age = 0
min_age = 100
oldest_child = ''
youngest_child = ''

# Перебираем каждую строку файла и ищем самого старшего и младшего ребенка
for line in lines:
    surname, name, age = line.split()
    age = int(age)
    if age > max_age:
        max_age = age
        oldest_child = line
    if age < min_age:
        min_age = age
        youngest_child = line

# Записываем информацию о самом старшем ребенке в файл
with open('самый_старший.txt', 'w') as file:
    file.write(oldest_child)

# Записываем информацию о самом младшем ребенке в файл
with open('самый_младший.txt', 'w') as file:
    file.write(youngest_child)
