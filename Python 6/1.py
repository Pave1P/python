import csv
import os
import random


def load_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


def show(data, output_type='top', num_rows=5, separator=','):
    if output_type == 'bottom':
        start_index = len(data) - num_rows
    elif output_type == 'random':
        start_index = random.randint(0, len(data) - num_rows)
    else:
        start_index = 0

    end_index = min(start_index + num_rows, len(data))
    for i in range(start_index, end_index):
        print(separator.join(data[i]))


def info(data):
    num_rows = len(data) - 1
    num_columns = len(data[0])
    print(f'Number of rows: {num_rows}x{num_columns}')

    header = data[0]
    for i, col_name in enumerate(header):
        non_empty_count = sum(1 for row in data[1:] if row[i])
        col_type = type(data[1][i]).__name__
        print(f'{col_name}  {non_empty_count}  {col_type}')


def del_nan(data):
    cleaned_data = [data[0]]
    for row in data[1:]:
        if all(row):
            cleaned_data.append(row)
    return cleaned_data


def make_ds(data, ratio=0.7):
    num_train = int(len(data) * ratio)

    learning_data = [data[0]] + data[1:num_train + 1]
    testing_data = [data[0]] + data[num_train + 1:]

    os.makedirs('workdata/Learning', exist_ok=True)
    os.makedirs('workdata/Testing', exist_ok=True)

    with open('workdata/Learning/train.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(learning_data)

    with open('workdata/Testing/test.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(testing_data)


file_path = 'data.csv'
data = load_file(file_path)

# Show the data
show(data, output_type='random', num_rows=5, separator=',')

# Info about the data
info(data)

# Delete rows with NaN values
cleaned_data = del_nan(data)

# Make training and testing datasets
make_ds(cleaned_data, ratio=0.7)