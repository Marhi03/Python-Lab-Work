#Write a Python program to find the frequency of elements in a list using a function.
#Create a list.
#Create a function that takes the list as input.
#Count frequency of each element inside the function.
#Return the result (e.g., dictionary) from the function.
#Display the result.

def frequency(lst):
    d={}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=input('Enter entry: ')
    lst.append(a)
print('List:', lst)
d=frequency(lst)
print(d)
