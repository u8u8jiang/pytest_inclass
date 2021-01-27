
time = int(input())

h = time//60 #in [0,23]
m = time - 60*h #in [0,59]

print(h,m)
