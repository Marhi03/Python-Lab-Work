n = int(input('Enter a number: '))
og=n
s=0
i=1
while(n>0):
    t=n%10
    s= s*i+t
    i=i*10
    n=n//10
if s==og:
    print('The given no. is palindrome.')
else:
    print('The given no. is not palindrome.')
