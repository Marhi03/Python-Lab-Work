#Create a list containing 5 strings and convert all the strings in the list to uppercase.

lst=[]
for i in range(0,5):
    s=input('Enter a string: ')
    lst.append(s.upper())
print(lst)
