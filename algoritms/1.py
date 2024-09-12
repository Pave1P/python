def check(s):
    s = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    # Проходим по каждому символу строки
    for char in s:
        if char in bracket_pairs.values():
            s.append(char)
        elif char in bracket_pairs.keys():
            if s == [] or s.pop() != bracket_pairs[char]:
                return "Строка не существует"

    # Если стек пуст по окончанию проверки, то все скобки сбалансированы
    return "Строка существует" if not s else "Строка не существует"


# Ввод строки
s = input("Введите строку: ")
# Проверяем строку
print(check(s))