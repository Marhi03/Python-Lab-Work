#Write a Python program to find the maximum and minimum values in a list using
#function.
#Create a list of numbers.
#Create a function that takes the list as input.
#Find maximum and minimum inside the function.
#Return both values from the function.
#Display the results.

def max_min(lst):
    for i in lst:
        minimum=i
        for j in lst:
            if j<minimum:
                minimum=j
    for i in lst:
        maximum=i
        for j in lst:
            if j>maximum:
                maximum=j
    return minimum,maximum

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter value: '))
    lst.append(a)
print('List:', lst)
m1,m2=max_min(lst)
print('Maximum and minimum values in the list are:', m2,m1)
