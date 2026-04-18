#Write a Python program to find numbers in a list that have an even number of digits
#using a function.
#Accept a list of integers from the user.
#Create a function that returns a list of numbers with even digits.
#Display the result.

def even_digits(lst):
    lstn=[]
    for i in lst:
        n=i
        d=0
        while n>0:
            d=d+1
            n=n//10
        if d%2==0:
            lstn.append(i)
    return lstn

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=even_digits(lst)
print('List of no. having even digits:', lstn)
