#Write a program that defines a function count_lower_upper() that accepts a string
#and calculates the number of uppercase and lowercase alphabets in it. It should
#return these values as a dictionary. Call this function for some sample string.

def count_lower_upper():
    d={'lower':0, 'upper':0}
    s=input('Enter a string: ')
    for ch in s:
        if 97<=ord(ch)<=122:
            d['lower']+=1
        if 65<=ord(ch)<=90:
            d['upper']+=1
    print(d)

count_lower_upper()
