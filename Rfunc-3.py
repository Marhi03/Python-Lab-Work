#A string is entered through the keyboard. Write a recursive function that counts the
#number of vowels in this string.

def vowels(s,i):
    v=0
    if i>=len(s):
        return 0
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        v=v+1
    if s[i]=='a'or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        v=v+1
    return v + vowels(s,(i+1))

s=input('Enter a string: ')
v=vowels(s,0)
print('No. of vowels:', v)
