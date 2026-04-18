#Write a Python program to calculate the power of a number using a function.
#Accept a base and an exponent from the user.
#Create a function that takes both values as input.
#Calculate the power inside the function.
#Return the result from the function.
#Display the result.

def power(a,b):
    e=a**b
    return e
a=int(input('Enter the base no.: '))
b=int(input('To what power should the base be raised: '))
e=power(a,b)
print('Ans:', e)

def Rpower(a,b):
    if b==0:
        return 1
    return a*Rpower(a,b-1)
r=Rpower(a,b)
print('Ans:', r)
