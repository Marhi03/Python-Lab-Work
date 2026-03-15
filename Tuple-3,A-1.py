#Represent a date using a tuple in the format (day, month, year). Create two such
#date tuples andwrite a program to calculate the number of days between the two dates

d1=int(input('Enter the day of the first date: '))
m1=int(input('Enter the month of the first date: '))
y1=int(input('Enter the year of the first date: '))
d2=int(input('Enter the day of the second date: '))
m2=int(input('Enter the month of the second date: '))
y2=int(input('Enter the year of the second date: '))

date1=(d1, m1, y1)
date2=(d2, m2, y2)
print('First date:', date1)
print('Second date:', date2)
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]

t1 = d1
for i in range(0, m1-1):
    t1 = t1 + days_in_month[i]
t1 = t1 + y1*365 + y1//4 - y1//100 + y1//400

t2 = d2
for i in range(0, m2-1):
    t2 = t2 + days_in_month[i]
t2 = t2 + y2*365 + y2//4 - y2//100 + y2//400

days = t1 - t2
if days < 0:
    days = -days

print("Number of days between the two dates:", days)
