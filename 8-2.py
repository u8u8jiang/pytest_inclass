# find the maximal element and print its row number and column number.
row, col =  [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(row)]
m = max(a)

for i in range(row):
    for j in range(col):
        a[i][j] *= mul
for row in a:
    print(*row)
