lst=[]
print('1. Inserting an element')
print('2. Deleting an element')
print('3. Display the queue')
print('4. Exit')
while 1:
    c=int(input('Enter your choice: '))
    if c==1:
        n=int(input('Enter the value to be inserted.'))
        lst.append(n)
    elif c==2:
              lst.pop(0)
    elif c==3:
              print(lst)
    elif c==4:
        break

