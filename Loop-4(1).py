n = int(input('Enter a number: '))
c=0
og=n
n1=n
for i in range(2,n):
    if(n%i == 0):
        c=c+1
if c==0:
    print('The given no. is prime')
else:
    print('The given no. is not prime')
d=0
s=0
while(n>0):
    d=d+1
    n=n//10
while(n1>0):
    t = n%10
    s = s+t*d
if s==og:
    print('The given no. is armstrong.')
else:
    print('The given no. is not armstrong.')
