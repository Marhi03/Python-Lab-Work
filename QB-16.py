#Write a Python program to calculate the factorial of a given number using recursive
#function. The program should:
#Accept a non-negative integer n from the user.
#Use a recursive function to compute the factorial.
#Display the factorial of the given number.

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

n=int(input('Enter a no. to find its factorial: '))
f=factorial(n)
print('Factorial of', n, 'is', f)
    
