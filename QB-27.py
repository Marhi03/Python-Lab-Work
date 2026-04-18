#Write a Python program to sort a list using a function.
#Create a list of numbers.
#Create a function that takes the list as input.
#Sort the list inside the function.
#Return the sorted list from the function.
#Display the result.

def sort(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            if lst[i]<lst[j]:
                t=lst[i]
                lst[i]=lst[j]
                lst[j]=t
    return lst

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('Original list:', lst)
lstn=sort(lst)
print('Sorted list:', lstn)
