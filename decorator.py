
import functools


class MyDecorator(object):
    FUNC = []

    def __init__(self, func, msg="SECOND"):
        self.FUNC.append(func)
        self.msg = msg

    def another(self, func):
        this_class = type(self)
        return this_class(func, msg="HELLO")

    def __call__(self, *args, **kwargs):
        for f in self.FUNC:
            f(self.msg)


# Decorate a function with a class objcet.
@MyDecorator
def just_a_name(*args, **kwargs):
    print('just_a_name: ', args)


just_a_name()


# Decorate a function with a method.
@just_a_name.another
def another_name(*args, **kwargs):
    print('another_name: ', args)


another_name()


def decorator_func(func):
    wrapped = func

    print('decorating: ', wrapped.__name__)
    wrapped.name = 'func'
    wrapped.bar = 'bar'

    @functools.wraps(wrapped)
    def inner_wrapper(*args, **kwargs):
        return wrapped(*args, **kwargs)

    return inner_wrapper
    # return functools.update_wrapper(wrapper, wrapped)


@decorator_func
def func_foo(a, b):
    """func doc"""
    print(a + b)


print(func_foo.__name__)
print(func_foo.__dict__)
func_foo('x', 'y')

