#Write a Python program to count even and odd numbers in a list using a function.
#Create a list of integers.
#Create a function that takes the list as input.
#Count even and odd numbers inside the function.
#Return both counts from the function.
#Display the results.

def count(lst):
    odd=0
    even=0
    for i in lst:
        if i%2==0:
            even+=1
        if i%2!=0:
            odd+=1
    return odd,even

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('List:', lst)
odd, even=count(lst)
print('No. of odd no.s are:', odd)
print('No. of even no.s are:', even)
