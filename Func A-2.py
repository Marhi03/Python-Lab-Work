#Write a recursive function to obtain length of a given string.

def length(s):
    l=0
    if s=='':
        return 0
    l=l+1
    return l + length(s[1:])

s=input('Enter a string: ')
l=length(s)
print('String:', s)
print('Length:', l)
