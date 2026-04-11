#Write a recursive function that reverses the list of numbers that it receives.

def revese(lst,l,i):
    if i>=l:
        return[]
    return [lst[l-i-1]] + revese(lst,l,i+1)

n=int(input('How many entries do you want to enter?: '))
lst=[]
for i in range(0,n):
    a=int(input('Enter the no.: '))
    lst.append(a)
print('Original list:', lst)
lstr=[]
l=len(lst)
lstr=revese(lst,l,0)
print('Reversed list:', lstr)
