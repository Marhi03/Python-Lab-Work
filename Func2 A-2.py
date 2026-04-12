#Two lists: [1,2,3,4,5,6] and [6,5,4,3,2,1]. Use map + lambda to add corresponding
#elements.

lst1=[1,2,3,4,5,6]
lst2=[6,5,4,3,2,1]
f=list(map(lambda a,b: a+b, lst1, lst2))
print('Addition list:', f)
