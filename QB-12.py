#Write a Python program to remove all vowels from a string using a function.
#Accept a string from the user.
#Create a function that returns the string after removing vowels.
#Display the result.

def remove_vowels(s):
    for ch in s:
        if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            s=s.replace(ch,'')
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            s=s.replace(ch,'')
    return s

s=input('Enter a string: ')
sn=remove_vowels(s)
print('String without vowels:', sn)
