#Write a program that defines a function called frequency() which computes the
#frequency of words present in a string passed to it. The frequencies should be
#returned in sorted order of words in the string.

def frequency(s):
    lst=list(s.split())
    set1=set(lst)
    d={}
    for i in set1:
        d[i]=0
    for i in lst:
        d[i]+=1
    dn=sorted(d.items())
    print(dn)

s=input('Enter a string: ')
frequency(s)
