#Write a program that accepts two strings and checks whether one string is present inside the other string.

s1 = input('Enter a string: ')
s2 = input('Enter another string: ')
if(s1 in s2):
    print(s1, 'is in', s2)
if(s2 in s1):
    print(s2, 'is in', s1)
