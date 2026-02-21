n = int(input('Enter a number: '))
c=0
for i in range(2,n):
    if(n%i == 0):
        c=c+1
if c==0:
    print('The given no. is prime')
else:
    print('The given no. is not prime')
