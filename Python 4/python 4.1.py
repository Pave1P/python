s=[int(i) for i in input().split(',')]
a=set()
for i in range(len(s)):
    a.add(s[i])
print(len(a))