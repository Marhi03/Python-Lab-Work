s = input('Enter a string: ')
su=''
for ch in s:
    n=ord(ch)
    if 97<=n<=122:
        n=n-32
    su=su+chr(n)
print('String in upper case:', su)

sl=''
for ch in s:
    n=ord(ch)
    if 65<=n<=90:
        n=n+32
    sl=sl+chr(n)
print('String in lower case:', sl)

st=''
for ch in s:
    n=ord(ch)
    if 97<=n<=122:
        n=n-32
    elif 65<=n<=90:
        n=n+32
    st=st+chr(n)
print('String in toggle case:', st)
