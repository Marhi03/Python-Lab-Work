#Write a function to create and return a list containing tuples of the 
#form (x,x²,x³) for all x between 1 and given ending value (both inclusive).

def function():
    n=int(input('Enter a no.: '))
    lst=[]
    for i in range(1,(n+1)):
        tpl=(i,i**2,i**3)
        lst.append(tpl)
    print(lst)
function()
