#Write a program that accepts a string from the user and prints the following:
#First character, Last character, Middle character (only if the string length is odd)

s = input('Enter a string: ')
n=len(s)
m=n//2
if n%2==0:
    print('First character:', s[0])
    print('Last character:', s[-1])
if n%2!=0:
    print('First character:', s[0])
    print('Last character:', s[-1])
    print('Middle character:', s[m])
