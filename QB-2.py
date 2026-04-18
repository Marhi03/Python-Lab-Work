#Write a Python program to find all palindrome numbers in a list using a function.
#Accept a list of integers from the user.
#Create a function that returns a list of palindrome numbers.
#Display the result.

def palindrome(lst):
    for i in lst:
        a=str(i)
        b=a[::-1]
        if a==b:
            p=int(a)
            print(p,'is a palindrome number.')

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
palindrome(lst)
