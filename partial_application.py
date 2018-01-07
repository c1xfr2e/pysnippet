
import functools


def func(a, b, c):
    return a + b + c


def ffoo(*args, **kwargs):
    print(args, kwargs)


x = functools.partial(func, 1)
print(x(2, c=3))

y = functools.partial(ffoo, 'hello', 123)
y(other='others')
