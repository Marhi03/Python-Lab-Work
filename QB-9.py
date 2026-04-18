#Write a Python program to find the factorial of each number in a list using a higher order
#function.
#Accept a list of non-negative integers.
#Create a function that returns a new list containing factorials of the original
#numbers.
#Display the result.

def factorial(lst):
    lstf=[]
    for i in lst:
        f=1
        for j in range(i,1,-1):
            f=f*j
        lstf.append(f)
    return lstf

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter non-negative no.: '))
    lst.append(a)
print('Original list:', lst)
lstf=factorial(lst)
print('Factorial:', lstf)
