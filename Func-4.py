#Write a program that defines a function sum_avg() to accept marks of five subjects and 
#calculates total and average. It should return directly both values.

def sum_avg(m1,m2,m3,m4,m5):
    s=m1+m2+m3+m4+m5
    avg=(m1+m2+m3+m4+m5)/5
    return(s, avg)
s1=int(input('Enter the marks of 1st subject: '))
s2=int(input('Enter the marks of 2nd subject: '))
s3=int(input('Enter the marks of 3rd subject: '))
s4=int(input('Enter the marks of 4th subject: '))
s5=int(input('Enter the marks of 5th subject: '))
s, avg = sum_avg(s1,s2,s3,s4,s5)
print('Sum of all marks is:', s)
print('Average marks in five subjects is:', avg)

