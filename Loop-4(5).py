#Write a program to check whether a given number is: Automorphic

n=int(input('Enter a number: '))
sq=n**2
og=n
d=0
ogsq=sq
s=0
while n>0:
    d=d+1
    n=n//10
for i in range(0,d):
    t=sq%10
    s=s+t*(10**i)
    sq=sq//10
if og==s:
    print('The given no. is automorphic.')
else:
    print('The given no. is not automorphic.')
