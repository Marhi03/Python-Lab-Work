#A positive integer is entered through the keyboard. Write a function to find its
#binary equivalent of this number.

def binary_eq(n):
    if n==0:
        return ('')
    return binary_eq(n//2) + str(n%2)

n=int(input('Enter a no.: '))
s=binary_eq(n)
print(s)
