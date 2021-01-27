x = int(input())

x1 = x//100
x2 = x//10 - 10*x1
x3 = x - 100*x1 - 10*x2

if x1<x2<x3:
    print('YES')
else:
    print('NO')

