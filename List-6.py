lstf=[]
n = int(input('Enter the no. of entries: '))
for i in range(0,n):
    a=int(input('Enter the value: '))
    lstf.append(a)
print('Degrees in fahreinheit are:')
print(lstf)
lstc=[]
for i in lstf:
    b=(5/9)*(i-32)
    lstc.append(round(b,2))
print('Degrees in celsius are:')
print(lstc)
