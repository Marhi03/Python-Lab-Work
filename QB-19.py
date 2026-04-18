#Write a Python program to perform slicing operations on a list. The program should:
#Create a list of at least 10 elements (numbers or strings).
#Display the following using slicing:
#First 5 elements
#Last 5 elements
#Elements from index 2 to 7
#Every alternate element from the list
#Display each result clearly.

n=int(input('How mant elements do you want to store(more than 10): '))
lst=[]
for i in range(0,n):
    a=input('Enter the entry: ')
    lst.append(a)
print('Entire list:', lst)
print('First 5 elements:', lst[0:5])
print('Last 5 elements:', lst[n:(n-6):-1])
print('Elements from index 2 to 7:', lst[2:8])
print('Alternate elements:', lst[0:(n+1):2])
