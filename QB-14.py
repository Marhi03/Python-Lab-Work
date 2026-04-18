#Write a Python program to find all pairs of numbers in a list whose sum equals a
#given number using a function.
#Accept a list of integers and a target sum from the user.
#Create a function that returns a list of tuples, each representing a pair.
#Display the result.

def sum(lst,n):
    lstn=[]
    for i in lst:
        for j in lst:
            if i+j==n:
                tpl=(i,j)
                lstn.append(tpl)
    return lstn

n=int(input('What should the sum be?: '))
lst=[]
e=int(input('How many entries do you want to store?: '))
for i in range(0,e):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=sum(lst,n)
print('Pair of no. equal to sum is:', lstn)
