lst1=[]
lst2=[]
lst3=[]
e1=int(input('How many entries for list 1: '))
e2=int(input('How many entries for list 2: '))
for i in range(0,e1):
    n=int(input('Enter the value for list 1: '))
    lst1.append(n)
for i in range(0,e2):
    n=int(input('Enter the value for list 2: '))
    lst2.append(n)
print(lst1)
print(lst2)
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print('New list:')
print(lst3)

