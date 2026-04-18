#Write a Python program to create a list of numbers and find the sum of all elements
#using a function. The program should:
#Accept list elements from the user.
#Create a function that takes the list as a parameter.
#Calculate the sum of all elements inside the function.
#Return the sum from the function.
#Display the final sum.

def sum(lst):
    s=0
    for i in lst:
        s=s+i
    return s

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('List:', lst)
s=sum(lst)
print('Sum of elements:', s)
    
