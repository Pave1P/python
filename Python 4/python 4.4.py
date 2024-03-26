text = input()
words = text.split()
count = {}

for word in words:
    if word in count:
        print(count[word], end=' ')
    else:
        print(0, end=' ')
    count[word] = count.get(word, 0) + 1