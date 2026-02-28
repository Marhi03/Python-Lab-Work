import random
lst=[]
lstp=[]
lstn=[]
a=0
for i in range(0,30):
    a = random.randint(-50,50)
    lst.append(a)
print(lst)
for i in lst:
    if i>0:
       lstp.append(i)
    elif i==0:
        lstp.append(i)
    else:
        lstn.append(i)
print(lstp)
print(lstn)
