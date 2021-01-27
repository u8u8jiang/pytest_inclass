x = int(input())

x1 = x//1000
x2 = x//100 - 10*x1
x3 = x//10 - 100*x1 - 10*x2
x4 = x - 1000*x1 - 100*x2 - 10*x3

if x1 == x4 and x2 == x3:
    print('YES')
else:
    print('NO')
