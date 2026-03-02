tpl=()
tpln=()
n=int(input('Enter the no. of entries: '))
for i in range(0,n):
    a=int(input('Enter value: '))
    tpl=tpl+(a,)
print('Original tuple:', tpl)

r=int(input('Which value is to be removed?: '))
for i in tpl:
    if r!=i:
        tpln=tpln+(i,)
print('Modified Tuple:', tpln)
