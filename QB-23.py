#Write a Python program to remove duplicate elements from a list using a function.
#Create a list with repeated elements.
#Create a function that takes the list as input.
#Remove duplicates inside the function.
#Return the updated list from the function.
#Display the result.

def no_duplicate(lst):
    lstn=[]
    for i in lst:
        if i not in lstn:
            lstn.append(i)
    return lstn

n=int(input('How many entries do you want to have?: '))
lst=[]
for i in range(0,n):
    a=input('Enter entry: ')
    lst.append(a)
print('Original list:', lst)
lstn=no_duplicate(lst)
print('Updated list:', lstn)
