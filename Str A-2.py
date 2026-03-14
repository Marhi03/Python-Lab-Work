s = input('Enter a string: ')
sr = input('Enter the string to be removed: ')
if (sr in s):
    sf = s.replace(sr, '')
    print(sf)
else:
    print(sr, 'is not the part of', s)
