# Fibonacci numbers,
#  Given a positive integer n, print the nth Fibonacci number.

n = int(input())
a = 1 
b = 1

i = 3
while  i<=n:
    a,b = b,a+b
    i +=1
print(b, end=' ')