import csv
import os
import random


def load_csv(file_path):
    if not os.path.isfile(file_path):
        print("Файл не найден.")
        return None

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    return data

def show(data, output_type="top", num_rows=5, separator=","):

    if not data:
        return

    if output_type == "bottom":
        data = data[-num_rows:]
    elif output_type == "random":
        data = random.sample(data, min(num_rows, len(data)))
    else:
        data = data[:num_rows]

    for row in data:
        print(separator.join(row))


def info(data, separator=","):
    if not data:
        return

    header = data[0]
    data = data[1:]

    num_rows = len(data)
    num_cols = len(header)

    print(f"Количество строк с данными: {num_rows}x{num_cols}")

    for i, field in enumerate(header):
        non_empty_count = sum(1 for row in data if row[i])
        field_type = "string" if all(isinstance(row[i], str) for row in data) else "int"
        print(f"{field:10} {non_empty_count:5} {field_type}")


def del_nan(data):
    if not data:
        return

    header = data[0]
    data = data[1:]

    cleaned_data = [header]
    for row in data:
        if all(row):
            cleaned_data.append(row)

    return cleaned_data


def make_ds(file_path):

    data = load_csv(file_path)
    if not data:
        return

    output_dir = os.path.join(os.path.dirname(file_path), "workdata")
    learning_dir = os.path.join(output_dir, "Learning")
    testing_dir = os.path.join(output_dir, "Testing")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(learning_dir):
        os.makedirs(learning_dir)
    if not os.path.exists(testing_dir):
        os.makedirs(testing_dir)

    random.shuffle(data)
    split_index = int(len(data) * 0.7)

    learning_data = data[:split_index]
    testing_data = data[split_index:]

    with open(os.path.join(learning_dir, "train.csv"), 'w', newline='', encoding='utf-8') as learning_file:
        writer = csv.writer(learning_file)
        writer.writerows(learning_data)

    with open(os.path.join(testing_dir, "test.csv"), 'w', newline='', encoding='utf-8') as testing_file:
        writer = csv.writer(testing_file)
        writer.writerows(testing_data)


# Пример использования функций:
file_path = "Titanic.csv"

# Загрузка CSV файла
data = load_csv(file_path)

# Показать данные CSV файла
show(data, output_type="random", num_rows=10, separator=",")

# Получить информацию о данных CSV файла
info(data)

# Удалить строки с пустыми значениями
cleaned_data = del_nan(data)

# Создать обучающий и тестовый наборы данных
make_ds(file_path)