#A list contains names of Faculty Members. Write a program to filter out those names
#whose length is more than 8 characters.

n=int(input('How many names do you want to enter?: '))
lst=[]
for i in range(0,n):
    s=input('Enter name: ')
    lst.append(s)
print('Original list:', lst)
f=list(filter(lambda s: len(s)>8, lst))
print('Filtered list:', f)
