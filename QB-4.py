#Write a Python program to count the number of vowels and consonants in a string
#using function.
#Accept a string from the user.
#Create a function that returns both counts.
#Display the result.

def count(s):
    sp=0
    v=0
    for ch in s:
        if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            v=v+1
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            v=v+1
        if ch==' ':
            sp=sp+1
    c=len(s)-v-sp
    return c,v

s=input('Enter a string: ')
c,v=count(s)
print('No. of consonants and vowels are:', c, ',', v)
