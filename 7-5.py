a = [int(i) for i in input().split()]

count = 0
for i in range(i,len(a)-1):
    if a[i] > a[i-1] and a[i] >a[i+1]:
        count +=1
print(count)