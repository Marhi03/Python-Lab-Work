#Write a Python program to print the Fibonacci series up to the nth term using a
#recursive function. The program should:
#Accept a positive integer n from the user.
#Use a recursive function to generate Fibonacci numbers.
#Display the Fibonacci series up to n terms.

def fibonacci(n,a1,a2):
    if n<=0:
        return[]
    lst=[]
    a3=a2+a1
    lst.append(a3)
    a1=a2
    a2=a3
    return lst + fibonacci(n-1,a1,a2) 

n=int(input('How many terms of the series do you want?: '))
lst=fibonacci(n-2,0,1)
lst.insert(0,0)
lst.insert(1,1)
print(lst)
