#Write a recursive function to obtain average of all numbers present in a given list.

def avg(lst, i):
    a=0
    if i>=len(lst):
        return 0
    a=lst[i]/len(lst)
    return a + avg(lst, i+1)

n=int(input('How many values do you want to store?: '))
lst=[]
for i in range(0,n):
    b=int(input('Enter the value: '))
    lst.append(b)
print('List:', lst)
a=avg(lst,0)
print('Average:', a)
