#Create a list of tuples containing a food item and its price.
#Sort the tuples in descending order by price.

n=int(input('How many entries do you want to store?: '))
lst=[]
for i in range(0,n):
    a=input('Enter food item: ')
    b=int(input('Enter price: '))
    tpli=(a, b)
    lst.append(tpli)

for i in range(0,n):
    for j in range(i,n):
        if lst[i][1]<lst[j][1]:
            t=lst[i]
            lst[i]=lst[j]
            lst[j]=t
            
print(lst)
