#Write a function create_list() that creates and returns a list which is an
#intersection of two lists passed to it.

def create_list(lst1, lst2):
    lstn=[]
    set1=set(lst1)
    set2=set(lst2)
    set3=set1.intersection(set2)
    lstn=list(set3)
    return lstn

n1=int(input('How many entries do you want to store in list1?: '))
lst1=[]
for i in range(0,n1):
    a=int(input('Enter the value: '))
    lst1.append(a)
n2=int(input('How many entries do you want to store in list2?: '))
lst2=[]
for i in range(0,n2):
    b=int(input('Enter the value: '))
    lst2.append(b)
print('List1:', lst1)
print('List2:', lst2)
lst3=create_list(lst1, lst2)
print('Intersection:', lst3)
