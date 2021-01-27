
# array
a = [1,2,3]
#the result of two codes are the same
#1
for item in a:
    print(item, end=' ')
#2
print(*a)
#
a.append(4)
a=a+[5]
for item in a:
    print(item, end = ' ')
print(*a)

#list
s = input()
a = [int(i) for i in s.split()]
print(a)

