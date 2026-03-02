#Suppose a date is represented as a tuple(d,m,y).
#Create two date tuples and find the number of days between the two dates.

tpl1=()
tpl2=()
print('Enter date in dd,mm,yyyy format')

for i in range(0,3):
    n=int(input('\nEnter value for 1st date: '))
    tpl1=tpl1+(n,)
for i in range(0,3):
    n=int(input('\nEnter value for 2nd date: '))
    tpl2=tpl2+(n,)

print('\n1. It is not a leap year')
print('2. It is a leap year')
y1=int(input('Enter value for 1st date: '))
y2=int(input('Enter value for 2nd date: '))

print('\n1. Month has 30 days')
print('2. Month has 31 days')
print('3. Month has 28 days')
m1=int(input('Enter value for 1st date: '))
m2=int(input('Enter value for 2nd date: '))

if y1==1:
    if m1==m2==1:
        d=((tpl2[2]*365) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*30) + tpl1[0])
    elif m1==m2==2:
        d=((tpl2[2]*365) + (tpl2[1]*31) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*31) + tpl1[0])
    elif m1==m2==3:
        d=((tpl2[2]*365) + (tpl2[1]*28) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*28) + tpl1[0])
    elif m1==1 and m2==2:
        d=((tpl2[2]*365) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*31) + tpl1[0])
    elif m1==2 and m2==3:
        d=((tpl2[2]*365) + (tpl2[1]*31) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*28) + tpl1[0])
    elif m1==1 and m2==3:
        d=((tpl2[2]*365) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*365) + (tpl1[1]*28) + tpl1[0])

if y2==2:
    if m2==m1==1:
        d=((tpl2[2]*366) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*30) + tpl1[0])
    elif m2==m1==2:
        d=((tpl2[2]*366) + (tpl2[1]*31) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*31) + tpl1[0])
    elif m2==m1==3:
        d=((tpl2[2]*366) + (tpl2[1]*28) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*28) + tpl1[0])
    elif m1==1 and m2==2:
        d=((tpl2[2]*366) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*31) + tpl1[0])
    elif m1==2 and m2==3:
        d=((tpl2[2]*366) + (tpl2[1]*31) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*28) + tpl1[0])
    elif m1==1 and m2==3:
        d=((tpl2[2]*366) + (tpl2[1]*30) + tpl2[0]) - ((tpl1[2]*366) + (tpl1[1]*28) + tpl1[0])

print('\nNo. of days between the two dates are:', abs(d))
