#Write a Python program to remove all prime numbers from a list using a higher order
#function.
#Accept a list of integers from the user.
#Create a function that returns a list with all prime numbers removed.
#Display the result.

def no_prime(lst):
    lstn=[]
    for i in lst:
        c=0
        if i<=1:
            lstn.append(i)
        if i>1:
         for j in range(2,i):
            if i%j==0:
                c=c+1
        if c!=0:
            lstn.append(i)
    return lstn

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=no_prime(lst)
print('List without prime:', lstn)
