#Write a Python program to count the frequency of each character in a string using a
#function.
#Accept a string from the user.
#Create a function that returns a dictionary with characters as keys and their
#frequency as values.
#Display the result.

def frequency(s):
    d={}
    for ch in s:
        if ch in d:
            d[ch]+=1
        else:
            d[ch]=1
    return d

s=input('Enter a string: ')
d=frequency(s)
print(d)
