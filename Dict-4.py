s = input('Enter a string: ')
d = {}
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print('Character frequencies: ', d)
