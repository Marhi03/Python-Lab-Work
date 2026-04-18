#Write a Python program to generate all prime factors of a number using a function.
#Accept a number from the user.
#Create a function that returns a list of its prime factors.
#Display the result.

def prime_factors(n):
    lst=[]
    lstf=[]
    for i in range(2,n):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if c==0:
           lst.append(i)
    for i in lst:
        if n%i==0:
            lstf.append(i)
    return lstf

n=int(input('Enter a number: '))
lstf=prime_factors(n)
print('Prime factors are:', lstf)
