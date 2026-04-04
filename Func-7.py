#A palindrome is a word or phrase that reads the same in both directions. Write a
#program that defines a function ispalindrome() which checks whether a given stringis
#a palindrome or not. Ignore spaces and case mismatch while checking for palindrome.

def ispalindrome(s):
    sl=s.lower()
    st=sl.replace(' ', '')
    sr=st[::-1]
    if st==sr:
        print('The given string is palindrome.')
    else:
        print('The given string is not palindrome.')

s=input('Enter a string: ')
ispalindrome(s)
