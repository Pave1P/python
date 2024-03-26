text = input()
words = text.split()
word_counts = {}

for word in words:
    word = word.strip('.,!?"').lower()
    if word:
        if word not in word_counts:
            word_counts[word] = 0
            word_counts[word] += 1
            sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word)