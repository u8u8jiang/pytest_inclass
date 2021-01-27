# https://snakify.org/en/lessons/two_dimensional_lists_arrays/steps/5/

n = 3
m = 4
a = [[0] * m for  i in range(n)]
print(a)
a[0][0] = 5
print(a)