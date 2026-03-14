s = input('Enter a string: ')
print('Accessing using +ve index.')
i=0
while i<len(s):
    print(s[i])
    i=i+1
print('Accessing using -ve index.')
for i in range(-(len(s)), 0):
    print(s[i])
