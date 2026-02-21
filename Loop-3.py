s = input('Enter a string: ')
c=0
d=0
for ch in s:
    if 97<=ord(ch)<=122:
        c=c+1
for ch in s:
    if 65<=ord(ch)<=90:
        c=c+1
for ch in s:
    if 48<=ord(ch)<=57:
        d=d+1
print('No. of alphabets are:', c)
print('No. of digits are:', d)
