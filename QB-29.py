#Write a Python program to count the number of vowels in a string using a function.
#Accept a string from the user.
#Create a function that takes the string as input.
#Count vowels inside the function.
#Return the count from the function.
#Display the result.

def count_vowels(s):
    v=0
    for ch in s:
        if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
            v=v+1
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            v=v+1
    return v

s=input('Enter a string: ')
v=count_vowels(s)
print('No. of vowels in the given string are:', v)
