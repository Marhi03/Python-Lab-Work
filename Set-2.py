s1=set()
s2=set()
print('To stop entering data for first day enter @')
i=0
while i!='@':
    i=input('Enter the id: ')
    if i!='@':
      s1.add(i)
print('First day data:', s1)

print('To stop entering data for second day enter $')
i=0
while i!='$':
    i=input('Enter the id: ')
    if i!='$':
      s2.add(i)
print('Second day data:', s2)

print('Visitors who visited both days:', s1&s2)
print('Visitors who visited only one of the days:', s1^s2)
print('Unique visitors across both days:', s1^s2 | s1&s2)
