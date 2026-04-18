#Write a Python program to reverse each word in a sentence using a function.
#Accept a sentence from the user.
#Create a function that returns the sentence with each word reversed but in the
#original order.
#Display the result.

def reverse(s):
    lst=s.split()
    lstn=[]
    for i in lst:
        a=i[::-1]
        lstn.append(a)
    sn=' '.join(lstn)
    return sn

s=input('Enter a sentence: ')
print('Original sentence:', s)
sn=reverse(s)
print('Sentence with reverse words:', sn)
