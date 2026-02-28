lst=[]
print('1. Insert an element')
print('2. Delete an element')
print('3. Display the stack')
print('4. Exit')
while 1:
    c=int(input('Enter your choice: '))
    if c==1:
        n=int(input('Enter the value: '))
        lst.append(n)
    elif c==2:
        lst.pop()
    elif c==3:
        print(lst)
    elif c==4:
        break
