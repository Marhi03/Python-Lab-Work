#Write a program that defines a function convert() that receives a string containing
#a sequence of whitespace separated words and returns a string after removing all
#duplicate words and sorting them alphanumerically.

def convert(s):
    set1=set(s.split())
    lst=list(set1)
    lst.sort()
    print(lst)

s=input('Enter a string: ')
convert(s)
