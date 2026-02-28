import random
lst1=[]
a=0
for i in range(0,50):
    a = random.randint(1,30)
    lst1.append(a)
print(lst1)
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
print(lst2)
