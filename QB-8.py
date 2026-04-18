#Write a Python program to find all numbers divisible by a given number k in a list
#using a function.
#Accept a list of integers and k from the user.
#Create a function that returns a list of numbers divisible by k.
#Display the result.

def divisibility(lst,k):
    lstn=[]
    for i in lst:
        if i%k==0:
            lstn.append(i)
    return lstn

k=int(input('Enter the number to check divisibility: '))
n=int(input('How mant entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=divisibility(lst,k)
print('No. divisible by k:', lstn)
    
