#Calculate a^b where a and b received through the keyword using recursion.

def power(a,b,i):
    if i==b:
        return 1
    return a*power(a,b,i+1)

a=int(input('Enter the base no.: '))
b=int(input('Enter the no. to which it has to be raised: '))
p=power(a,b,0)
print(p)
