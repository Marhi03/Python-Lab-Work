#Remove empty tuple from list of tuples

n=int(input('How many entries do you want to store?: '))
lst=[]
tpl=()
for i in range(0,n):
        s=input('Enter the entry: ')
        if s=='':
            tpl=()
        else:
            tpl=(s,)
        lst.append(tpl)
print('Original list:', lst)
lstn=[]
for i in lst:
    if isinstance(i, tuple):
        if i:
            lstn.append(i)
print('List without empty tuples:', lstn)
