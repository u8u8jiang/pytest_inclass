# Determine the length of the sequence. The sequence ends with 0.
a = int(input())
i = 0
sum = 0
while a!=0:
    i+=1
    sum += a
    a = int(input())
print(i,sum)