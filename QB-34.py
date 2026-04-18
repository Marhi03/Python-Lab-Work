#Write a Python program to filter and display names from a list whose length is
#greater than 5 using the filter() function.

n=int(input('How many names do you want to store?: '))
lst=[]
for i in range(0,n):
    a=input('Enter name: ')
    lst.append(a)
print('Entire list:', lst)
f=list(filter(lambda a: len(a)>5, lst))
print('Names whose length is greater than 5:', f)
