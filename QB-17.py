#Write a Python program to check whether a person is eligible to vote or not using a
#function. The program should:
#Accept the age of the user as input.
#Create a function that takes age as a parameter.
#Determine whether the age is greater than or equal to 18.
#Display an appropriate message.

def eligibility(n):
    if n>=18:
        print('Eligible to vote.')
    else:
        print('Not eligible to vote.')

n=int(input('Enter age: '))
eligibility(n)
