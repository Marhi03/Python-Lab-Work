#Pangram is a sentence that uses every letter of the alphabet. Write a program to
#check whether a given string is pangram or not, through a user-defined function
#ispangram(). Test the function with “The quick brown fox jumps over the lazy dog” or
#“Crazy Fredrick bought many very exquisite opal jewels”.

def ispangram(s):
    sl=s.lower()
    sf=sl.replace(' ','')
    lst=list(sf)
    set1=set(lst)
    set2={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    if set2<=set1:
        print('Given string is pangram.')
    else:
        print('Given string is not pangram.')

s=input('Enter a string: ')
ispangram(s)
