n = int(input('Enter a number: '))
d=0
og=n
n1=n
s=0
while(n>0):
    d=d+1
    n=n//10
while(n1>0):
    t = n1%10
    s = s+t**d
    n1 = n1//10
if s==og:
    print('The given no. is armstrong.')
else:
    print('The given no. is not armstrong.')
