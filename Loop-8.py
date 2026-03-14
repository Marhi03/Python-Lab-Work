#Write a program to find the factorial of a given number.

n=int(input('Enter a number: '))
nf=1
for i in range(1,(n+1)):
    nf=nf*i
print('The factorial of', n, 'is:', nf)
