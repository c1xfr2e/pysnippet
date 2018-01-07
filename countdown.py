__author__ = 'zh'


def countdown(n):
    print('start countdown from: %d' % n)
    while n >= 0:
        newn = yield n
        if newn:
            n = newn
        else:
            n -= 1

iterable = countdown(3)
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))

cd = countdown(5)
for i in cd:
    print(i)
    if i == 5:
        cd.send(3)


cd2 = countdown(5)
while True:
    try:
        i = cd2.send(None)
        print(i)
        if i == 5:
            ret_send3 = cd2.send(3)
            print('ret of send(3): ', ret_send3)
    except StopIteration:
        print("StopIteration")
        break
