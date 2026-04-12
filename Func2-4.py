#Consider the following list: lst = ['madam','Python',"malayalam",12321]. Write a
#program to print those strings which are palindromes.

lst=['madam','Python',"malayalam",12321]
print('Original list:', lst)
f=list(filter(lambda s: str(s)==str(s)[::-1], lst))
print('Palindrome list:', f)
