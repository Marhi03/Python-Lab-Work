#Store three functions in a list and call them in a loop.

def func1():
    print('You are in func1().')
def func2():
    print('You are in func2().')
def func3():
    print('You are in func3().')
lst=[func1(), func2(), func3()]
for f in lst:
    f
