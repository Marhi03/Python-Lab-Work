#Remove duplicates from a list using a set.

lst=[]
lstn=[]
n=int(input('How many entries do you want to enter?: '))
for i in range(0,n):
    s=input('Enter the entry: ')
    lst.append(s)
print('Original list:', lst)
s=set(lst)
lstn=list(s)
print('List without duplicate items:', lstn)
