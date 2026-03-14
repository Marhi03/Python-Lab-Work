#Write a function that removes a specified substring from a given string if it exists.
#Example: onestring = "abcdef", removestring = "cd", The resulting string should be "abef".

s = input('Enter a string: ')
sr = input('Enter the string to be removed: ')
if (sr in s):
    sf = s.replace(sr, '')
    print(sf)
else:
    print(sr, 'is not the part of', s)
