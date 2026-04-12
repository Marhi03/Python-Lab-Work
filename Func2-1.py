#Define three functions fun(), disp() and msg(). Store them in a list and call them
#one by one in a loop.

def fun():
    print('You are in fun() function.')
def disp():
    print('You are in disp() function.')
def msg():
    print('You are in msg() function.')

lst=[fun(), disp(), msg()]
for f in lst:
    f
