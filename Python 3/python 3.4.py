def count_string(strings):
    counts = {}
    for i in strings:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return list(counts.values())


input_strings = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
print(*count_string(input_strings))

input_strings = ['aaa', 'bbb', 'ccc']
print(*count_string(input_strings))

input_strings = ['abc', 'abc', 'abc']
print(*count_string(input_strings))
