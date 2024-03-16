matrix = []
n=0
for i in range(3):
    row = input().split()
    for j in range(len(row)):
        row[j] = int(row[i])
    matrix.append(row[:3:])

for i in range(-100, 100):
    for j in range(-100, 100):
        for k in range(-100, 100):
            str1 = i * matrix[0][0] + j * matrix[0][1] + k * matrix[0][2]
            str2 = i * matrix[1][0] + j * matrix[1][1] + k * matrix[1][2]
            str3 = i * matrix[2][0] + j * matrix[2][1] + k * matrix[2][2]
            if str1 + str2 + str3 == 0:
                n = 1
            break
if n == 1:
    print("столбцы линейно зависимы ")
