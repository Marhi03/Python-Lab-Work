#Write a program that defines a function sum_avg() to accept marks of five subjects
#and calculates total and average. It should return directly both values.

def sum_avg(marks):
    s=0
    for i in marks:
        s=s+i
    avg=s/5
    return s, avg

marks=[]
for i in range(1,6):
    a=int(input('Enter marks: '))
    marks.append(a)
s, avg=sum_avg(marks)
print('Total marks:', s)
print('Average:', avg)
