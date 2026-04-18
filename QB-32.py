#Write a Python program to find the second largest number in a list using a function.
#Accept a list of numbers from the user.
#Create a function that takes the list as input.
#Find the second largest number inside the function.
#Return the second largest number from the function.
#Display the result.

def second_largest(lst):
    for i in lst:
        m=i
        for j in lst:
            if j>m:
                m=j
    lst.remove(m)
    for i in lst:
        m=i
        for j in lst:
            if j>m:
                m=j
    return m

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('List:', lst)
m=second_largest(lst)
print('Second largest value in list is:', m)
