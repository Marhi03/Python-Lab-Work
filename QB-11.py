#Write a Python program to calculate the sum of even numbers in a list using function
#Accept a list of integers from the user.
#Create a function that returns the sum of even numbers.
#Display the result.

def sum(lst):
    even=list(filter(lambda a: a%2==0, lst))
    s=0
    for i in even:
        s=s+i
    return s

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('List:', lst)
s=sum(lst)
print('Sum of even no. of the list is:', s)
