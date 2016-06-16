__author__ = 'zh'

import types


def add(x,y):
    yield x+y


def main():
    r = yield add(2,2)
    print r
    yield


def run():
    m = main()
    sub = m.send(None)
    result = sub.send(None)
    m.send(result)

mr = main()
print mr

run()

def gen1(a, b):
    print '            gen1 before yield'
    yield a + b
    print '            gen1 after yield'


def gen2(a, b):
    print '        gen2 before yield'
    ret = yield gen1(a*2, b*2)
    print '        gen2 after yield', ret
    yield ret


def top_fun(a, b):
    print '    top_fun before yield'
    ret = yield gen2(a, b)
    print '    top_fun after yield', ret
    yield ret


def do():
    r = yield top_fun(1, 2)
    print 'final result:', r


target = do()
sendval = None
stack = []
while True:
    try:
        result = target.send(sendval)
        print 'target.send result:', result
        if isinstance(result, types.GeneratorType):
            stack.append(target)
            sendval = None
            target = result
        else:
            if not stack:
                break
            sendval = result
            target = stack.pop()
    except StopIteration:
        if not stack:
            break
        sendval = None
        target = stack.pop()

print 'end'
