#Write a program that defines a function count_alpha_digits() that accepts a string
#and calculates the number of alphabets and digits in it. It should return these
#values as a dictionary.

def count_alpha_digits(s):
    d={'Alphabets':0, 'Digits':0}
    lst=list(s)
    for i in lst:
        if i.isalpha():
            d['Alphabets']+=1
        elif i.isalnum():
            d['Digits']+=1
    print(d)

s=input('Enter a string: ')
count_alpha_digits(s)
