alpha = int(input())  # the degree of hour

h = alpha//30 # the degree of a hour is 30 degree
alpha1 = int(alpha - 30*h)
beta = 12*alpha1   # 360/12(degree/hr)=360(degree/min)
print(beta)

