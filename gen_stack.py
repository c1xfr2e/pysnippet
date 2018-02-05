# coding: utf8
__author__ = 'zh'


import types


def sub(x, y):
    pass


def add(x, y):
    yield x + y


def main():
    r1 = yield add(1, 1)
    print(r1)
    r2 = yield add(r1, 100)
    print(r2)
    r3 = yield add(r2, 1000)
    print(r3)
    return r3


def run():
    main_gen = main()
    send_value = None
    sub_gen = main_gen.send(send_value)
    try:
        while True:
            if isinstance(sub_gen, types.GeneratorType):
                send_value = sub_gen.send(None)
            else:
                send_value = sub_gen
            sub_gen = main_gen.send(send_value)
    except StopIteration as stop_iter:
        return stop_iter.value


print("run:", run())


def gen1(a, b):
    print('------------ gen1 before yield')
    yield a + b
    print('------------ gen1 after yield')


def gen2(a, b):
    print('-------- gen2 before yield')
    ret = yield gen1(a*2, b*2)
    print('-------- gen2 after yield', ret)
    yield ret


def top_fun(a, b):
    print('---- top_fun before yield')
    ret = yield gen2(a, b)
    print('---- top_fun after yield', ret)
    ret = yield gen1(ret, 10000)
    return ret


def do():
    r = yield top_fun(1, 2)
    print('do result:', r)
    return r


target = do()
sendval = None
stack = []
while True:
    try:
        result = target.send(sendval)
        # print('target.send result:', result)
        if isinstance(result, types.GeneratorType):
            stack.append(target)
            sendval = None
            target = result
        else:
            if not stack:
                break
            sendval = result
            target = stack.pop()
    except StopIteration as si:
        if not stack:
            break
        sendval = si.value
        target = stack.pop()

print('the end')
