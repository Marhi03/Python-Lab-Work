#Write a Python program to check whether a number is prime using a function.
#Accept an integer from the user.
#Create a function that takes the number as input.
#Check if the number is prime inside the function.
#Return True or False from the function.
#Display the result.

def prime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if c==0:
        return 1
    else:
        return 0

n=int(input('Enter a no. to check if it is prime?: '))
r=prime(n)
if r:
    print(n, 'is a prime number.')
else:
    print(n, 'is not a prime number.')
