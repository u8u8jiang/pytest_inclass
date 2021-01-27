a = int(input())
i = 0
sum = 0
while a!=0:
    i+=1
    sum += a
    a = int(input())
print(sum/i) 
print("%.2f"%(sum/i))  # if the point too many, can shortly show it