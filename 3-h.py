# determine whether a queen can go from the first square 
# to the second one in a single move.
 
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1-x2) == 0 or abs(y1-y2) == 0:
    print("YES")
elif abs(x1-x2) == abs(y1-y2):
    print("YES")
else:
    print("NO")