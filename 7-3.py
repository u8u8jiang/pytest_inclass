a = [int(i) for i in input().split()]

for i in range(1,len(a)):
    if a[i-1] < a[i] :
        print(a[i],end=' ')
