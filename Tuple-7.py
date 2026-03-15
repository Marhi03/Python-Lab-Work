#Deleting an element by creating a new tuple.

n=int(input('How many entries do you want to store?: '))
tpl=()
lst=[]
tpln=()
for i in range(0,n):
    s=int(input('Enter the entry: '))
    tpl=tpl+(s,)
print('Original tuple:', tpl)
lst=list(tpl)


r=int(input('Which value do you want to remove: '))
for i in lst:
    if i==r:
        lst.remove(i)
tpln=tuple(lst)
print('Tuple after deleting the element:', tpln)
