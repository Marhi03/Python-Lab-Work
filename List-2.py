import random
lst = []
for i in range(0,20):
    a = random.randrange(1,50)
    lst.append(a)
print(lst)
n = int(input('Enter a number'))
for ele in lst:
    if (n!=ele):
        break
print('This value is not present in the list.')
for ele in lst:
    if(n==ele):
        print(lst.index(ele))
