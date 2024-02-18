c = int(input("Введите число:"))
n = 2 ** c

a = [[1] * i for i in range(1, n + 1)]

for i in range(n):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

for i in range(n):
    for j in range(i + 1):
        if a[i][j] % 2 == 0:
            a[i][j] = " "
        else:
            a[i][j] = "*"
    print(" " * (n - i - 1), end=" ")
    print(*a[i])