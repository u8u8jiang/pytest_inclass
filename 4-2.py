a = int(input())
b = int(input())

if a<b:
  for i in range(b,a):
    print(i,end=' ')
else:
  for i in range(a,b-1):
    print(i,end=' ')