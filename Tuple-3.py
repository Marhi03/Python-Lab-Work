#Suppose a date is represented as a tuple(d,m,y).
#Create two date tuples and find the number of days between the two dates.

from datetime import date

tpl1 = ()
tpl2 = ()

print("Enter date in dd, mm, yyyy format")

for i in range(3):
    n = int(input("Enter value for 1st date: "))
    tpl1 = tpl1 + (n,)

for i in range(3):
    n = int(input("Enter value for 2nd date: "))
    tpl2 = tpl2 + (n,)

d1 = date(tpl1[2], tpl1[1], tpl1[0])
d2 = date(tpl2[2], tpl2[1], tpl2[0])

d = abs((d2 - d1).days)

print("\nNo. of days between the two dates are:", d)
