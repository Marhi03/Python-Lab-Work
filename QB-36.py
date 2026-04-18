#Write a Python program to find all prime numbers in a list using a higher order
#function.
#Accept a list of integers from the user.
#Create a function that takes the list and returns a new list containing only prime
#numbers.
#Display the result.

def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if n==1:
        return False
    if c==0:
        return True
    return False

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Entire list:', lst)
f=list(filter(prime, lst))
print('Prime numbers:', f)
            
