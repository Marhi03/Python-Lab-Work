#Write a program to check whether a given number is: Perfect

n=int(input('Enter a number: '))
og=n
s=0
for i in range(1,n):
    t=n%i
    if(t==0):
        s=s+i
if s==og:
    print('The given no is perfect.')
else:
    print('The given no is not perfect.')
