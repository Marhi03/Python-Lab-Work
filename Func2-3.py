#Generate the list of 10 different random numbers between -15 and 15. Create a new
#list by obtaining square of all numbers in a list.

import random
lst=[]
s=set()
while len(s)<10:
    a=random.randrange(-15,15)
    s.add(a)
lst=list(s)
print('Original list:', lst)
f=list(map(lambda a:a*a, lst))
print('Squares:', f)
