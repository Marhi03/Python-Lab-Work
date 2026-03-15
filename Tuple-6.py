#Modify an element of a tuple by creating a new tuple.

n=int(input('How many elements do you want to store?: '))
tpl=()
lst=[]
tpln=()
for i in range(0,n):
    s=int(input('Enter the entry: '))
    tpl=tpl+(s,)
print('Original tuple:', tpl)

lst=list(tpl)
a=int(input('Which element do you want to modify?: '))
b=int(input('What value is to be placed there?: '))
index=lst.index(a)
lst[index]=b
tpln=tuple(lst)
print('Modified tuple:', tpln)
