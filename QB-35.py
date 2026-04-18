#Develop a Python program that takes a list of integers as input and finds the
#maximum number from the list using the reduce() function.

from functools import reduce
n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Data:', lst)
f=reduce(lambda a,b: a if a>b else b, lst)
print('Maximum value of list:', f)
