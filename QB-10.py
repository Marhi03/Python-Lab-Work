#Write a Python program to find common elements between two lists using a function.
#Accept two lists from the user.
#Create a function that returns a list of common elements.
#Display the result.

def common(lst1, lst2):
    set1=set(lst1)
    set2=set(lst2)
    lst=[]
    set3=set1.intersection(set2)
    lst=list(set3)
    return lst

n1=int(input('How many elements do you want to store in list1?: '))
lst1=[]
for i in range(0,n1):
    a=input('Enter value: ')
    lst1.append(a)
n2=int(input('How many elements do you want to store in list2?: '))
lst2=[]
for i in range(0,n2):
    b=input('Enter value: ')
    lst2.append(b)
print('List1:', lst1)
print('List2:', lst2)
lst=common(lst1, lst2)
print('Common elements:', lst)
