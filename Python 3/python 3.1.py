def compress_string(s):
    result = ""
    count = 1
    for i in range(len(s)):
        if i != len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            result += s[i] + str(count)
            count = 1
    return result.replace('1', '')


input_string = input()
print(compress_string(input_string))
