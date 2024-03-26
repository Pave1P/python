s=set(int(i) for i in input().split(','))
a=set(int(i) for i in input().split(','))
if s==a:
    print("False")
elif s.issubset(a):
    print('True')
else:
    print('False')