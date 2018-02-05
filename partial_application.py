
import functools


def func(a, b, c):
    print('a', a, 'b', b, 'c', c)
    return a + b + c


def ffoo(*args, **kwargs):
    print(args, kwargs)


pfunc = functools.partial(func, 2, c=3)
print(pfunc.__name__)
print(pfunc(1))

y = functools.partial(ffoo, 'hello', 123)
y(other='others')
