import datetime

def outer(start):
    state = start
    def inner(label):
        nonlocal state
        print((label, state))
        state += 1
    return inner

F = outer(0)
F('spam')
F('egg')

G = outer(100)
G('ham')

dt = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
