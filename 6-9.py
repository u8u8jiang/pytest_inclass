
a = int(input())
i = 0
a1 = 0
iMax=0
while a!=0:
    i+=1
    a = int(input())
    a = max(a,a1)
    if a != a1:
        iMax = i 

# print(a1,iMax)
print(iMax)



