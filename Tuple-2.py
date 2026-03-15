#A list contains tuples containing roll number, name, and age of students. Write a
#Python program to create three separate lists for roll numbers, names, and ages.

lst=[]
n=int(input('How many student details, do u want to store?: '))
for i in range(1,(n+1)):
    a=int(input('Enter roll no.: '))
    b=input('Enter name: ')
    c=int(input('Enter age: '))
    tpli=(a, b, c)
    lst.append(tpli)

lstr=[]
lstn=[]
lsta=[]
for i in range(0,n):
    lstr.append(lst[i][0])
    lstn.append(lst[i][1])
    lsta.append(lst[i][2])
print('List for roll no. is:', lstr)
print('List for name is:', lstn)
print('List for age is:', lsta)
