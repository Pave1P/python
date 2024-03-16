def decompress_string(s):
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        count = ""
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        result += char * int(count)
    return result


string = input("Введите строку для декодирования: ")
print(decompress_string(string))
