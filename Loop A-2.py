import math
d = int(input('Enter the angle in degrees: '))
sinx = 0
x = (3.14159/180)*d
for i in range(1,10,2):
    t = ((-1)**((i-1)//2))*((x**i)/math.factorial(i))
    sinx = sinx + t
print('Value of sin', d, 'is', sinx)
