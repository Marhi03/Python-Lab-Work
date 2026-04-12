#Suppose there are two lists, one containing numbers from 1to6, and other containing
#numbers from 6to1. Write a program to obtain a list that contains elements obtained
#by adding corresponding elements of the two lists.

lst1=[1,2,3,4,5,6]
lst2=[6,5,4,3,2,1]
f=list(map(lambda a,b: a+b, lst1, lst2))
print('Addition of two lists is:', f)
