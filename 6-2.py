#判斷大於1的最小公因數

num = int(input())
i=2 #1 isn't, so start from 2
while num%i != 0:
    i +=1  
print(i)

