#Write a Python program to calculate the square of numbers in a list using a function
#Accept numbers in a list.
#Create a function that takes the list as input.
#Compute squares inside the function.
#Return the new list with squared values.
#Display the result.

def square(lst):
    lstn=[]
    for i in lst:
        s=i**2
        lstn.append(s)
    return lstn

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=square(lst)
print('List of squares:', lstn)
