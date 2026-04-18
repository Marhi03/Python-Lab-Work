#Write a Python program to concatenate two lists using a function.
#Create two lists.
#Create a function that takes both lists as input.
#Concatenate them inside the function.
#Return the combined list from the function.
#Display the result.

def concatenate(lst1, lst2):
    return lst1+lst2

n1=int(input('How many entries do you want to store in list1?: '))
lst1=[]
for i in range(0,n1):
    a=input('Enter input: ')
    lst1.append(a)
n2=int(input('How many entries do you want to store in list2?: '))
lst2=[]
for i in range(0,n2):
    b=input('Enter input: ')
    lst2.append(b)
print('List1:', lst1)
print('List2:', lst2)
lstn=concatenate(lst1, lst2)
print('Concatenated list:', lstn)
