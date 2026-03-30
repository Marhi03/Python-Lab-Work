def compute():
    n=int(input('Enter a digit: '))
    s=0
    t=0
    for i in range(1,5):
      t=t*10 + n
      s=s+t
    print('Sum:', s)
compute()
