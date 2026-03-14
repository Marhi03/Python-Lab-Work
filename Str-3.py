#Write a Python program that accesses and prints each character of a string in both forward and reverse order using a while loop.

s = input('Enter a string: ')
print('Accessing using +ve index.')
i=0
while i<len(s):
    print(s[i])
    i=i+1
print('Accessing using -ve index.')
for i in range(-(len(s)), 0):
    print(s[i])
