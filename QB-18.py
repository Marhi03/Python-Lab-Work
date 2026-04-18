#Write a Python program to create a list of 10 random numbers and generate the cube
#of each number. The program should:
#Create a list containing 10 random numbers.
#Generate the cube of each number in the list.
#Store the cubed values in a new list.
#Display both the original list and the new list.

import random
def cube(lst):
    lstn=[]
    for i in lst:
        c=i**3
        lstn.append(c)
    return lstn

lst=[]
for i in range(0,10):
    a=random.randrange(0,100)
    lst.append(a)
print('Original list:', lst)
lstn=cube(lst)
print('List of cubes:', lstn)
