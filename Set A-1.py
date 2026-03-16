s1=set()
s2=set()
print('To stop entering data for 1st set enter #')
i=0
while i!='#':
    i=input('Enter the entry: ')
    if i!='#':
        s1.add(i)
print('Data of set 1:', s1)

print('To stop entering data for 2nd set enter @')
i=0
while i!='@':
    i=input('Enter the entry: ')
    if i!='@':
        s2.add(i)
print('Data of set 2:', s2)

print('Is first set a subset of second set:', s1<=s2)
print('Is second set a superset of first set:', s2>=s1)
print('Are both sets equal:', s1==s2)
