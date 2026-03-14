#Write a program that accepts a string from the user and counts the number of vowels present in it.

s = input('Enter a string: ')
c=0
C=0
for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        c=c+1
    if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        C=C+1
v = c + C
print('No. of vowels in', s, 'are:', v)
