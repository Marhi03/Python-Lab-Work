#Write a program that defines a function compute() that calculates the value 
#of n + nn + nnn + nnnn, where n is digit received by the function. test the function for digits 4 to 7.

def compute():
    n=int(input('Enter a digit: '))
    s=0
    t=0
    for i in range(1,5):
      t=t*10 + n
      s=s+t
    print('Sum:', s)
compute()
