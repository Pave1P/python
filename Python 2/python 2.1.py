n = int(input())
s=[]
for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=s[i-1][j-1]+s[i-1][j]
    s.append(row)

for r in s:
    print(*r)