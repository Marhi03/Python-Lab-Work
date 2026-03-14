#Create a list containing 5 odd integers generated using random numbers. 
#Similarly, create another list containing 4 even integers using random numbers. Replace the third element of the odd-integers 
#list with the list of 4 even integers. Then flatten the list, sort it, and print the final list. Display appropriate messages 
#at each stage.

import random
lst1 = []
for i in range(0,5):
    a = random.randrange(1,50,2)
    lst1.append(a)
print('Original odd list:', lst1)

lst2 = []
for i in range(0,4):
    a = random.randrange(0,50,2)
    lst2.append(a)
print('Original even list:', lst2)

lst1.pop(2)
lst1.insert(2, lst2)
print('New odd list is:', lst1)

lst1[2:3] = lst2
print('Flattened list is:', lst1)

lst1.sort()
print(lst1)
