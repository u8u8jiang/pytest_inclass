#  print the first adjacent pair of elements that have the same sign. 
a = [int(i) for i in input().split()]

for i in range(1,len(a)):
    if a[i-1] * a[i] > 0:
        print(a[i-1],a[i],end=' ')
        break
else:
    print(0)