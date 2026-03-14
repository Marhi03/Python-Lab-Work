n=int(input('Enter the value of n: '))
r=int(input('Enter the value of r: '))

nf=1
df=1
for i in range(1,(n+1)):
    nf=nf*i
d=n-r
for i in range(1,(d+1)):
    df=df*i
nPr=nf/df
print('nPr for given values is:', nPr)

rf=1
for i in range(1,(r+1)):
    rf=rf*i
nCr=nf/(rf*df)
print('nCr for given values is:', nCr)
