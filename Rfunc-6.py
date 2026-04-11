#A list contains some negative and some positive values. Write a recursive function
#that sanitizes the list by replacing all negative numbers with 0.

def non_negative(lst,i):
    if i>=len(lst):
        return []
    if lst[i]<0:
        lst[i]=0
    return [lst[i]] + non_negative(lst,i+1)

n=int(input('How many entries do you wan to store?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter the value: '))
    lst.append(a)
print('Original list:', lst)
lstn=[]
lstn=non_negative(lst,0)
print('New list:', lstn)
