#Write a Python program to remove duplicate words from a sentence using a function.
#Accept a sentence from the user.
#Create a function that returns the list without duplicates.
#Display the result.

def no_duplicates(s):
    lst=s.split()
    lstn=[]
    set1=set(lst)
    lstn=list(set1)
    return lstn

s=input('Enter a sentence: ')
lst=no_duplicates(s)
print('List without duplicates:', lst)
