n = int(input('How many terms to generate? '))
a1=0
a2=1
print(a1)
print(a2)
for i in range(1,(n-1)):
    a = a1+a2
    a1=a2
    a2=a
    print(a)
