def function():
    n=int(input('Enter a no.: '))
    lst=[]
    for i in range(1,(n+1)):
        tpl=(i,i**2,i**3)
        lst.append(tpl)
    print(lst)
function()
