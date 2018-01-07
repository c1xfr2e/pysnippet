def tester(start):
    state = start
    def nested(label):
        print((label, state))
        state += 1
    return nested

F = tester(0)
F('spam')
F('egg')

G = tester(1)
G('ham')