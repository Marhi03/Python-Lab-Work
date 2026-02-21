n = int(input('Enter the no.: '))
i=2
r=0
while i<=n:
    t = n%i
    if(t==0):
        r+=1
    i+=1
if(r==2):
    print(n, 'is a prime no.')
else:
    print(n, 'is not a prime no.')
