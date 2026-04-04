#Write a program that defines a function create_array() to create and return a 3D
#array whose dimensions are passed to the function. Also initialize each element of
#this array to a value passed to the function. e.g. create_array(3,4,5,n) where first
#three arguments are 3D array dimensions and 4th value is for initialing each value
#of the 3D array.

def create_array(l,r,c,n):
    a=[]
    for i in range(0,l):
        a1=[]
        for j in range(0,r):
            a2=[]
            for k in range(0,c):
                a2.append(n)
            a1.append(a2)
        a.append(a1)
    return(a)

l=int(input('How many layers?: '))
r=int(input('How many rows?: '))
c=int(input('How many columns?: '))
n=int(input('Which no. you want to enter?: '))
a=create_array(l,r,c,n)
print('3D array:', a)
