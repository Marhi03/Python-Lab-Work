#Write a Python program to count the frequency of each word in a sentence using a
#function.
#Accept a sentence from the user.
#Create a function that returns a dictionary with word frequencies.
#Display the result.

def frequency(s):
    d={}
    lst=s.split()
    for i in lst:
        if i in d:
           d[i]+=1
        else:
            d[i]=1
    return d

s=input('Enter a string: ')
d=frequency(s)
print(d)
    
