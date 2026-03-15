lst=['Riya', 'Neha', ('Om',), ('Arjun',), 'Sneha', ('Parth',), 'Vishva']
g=0
b=0
for i in lst:
    if isinstance(i, tuple):
        b=b+len(i)
    else:
        g=g+1
print('No. of girls:', g)
print('No. of boys:', b)
        
