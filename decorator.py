
import functools


class Decorator(object):
    def __init__(self, foo=None, bar=None):
        self.foo = foo
        self.bar = bar

    def another(self, fun):
        this_class = type(self)
        return this_class(self.foo, fun)


@Decorator
def just_a_name():
    print 'where does this line of code go?'

print just_a_name.__dict__


@just_a_name.another
def name_again():
    print 'wtf'

print name_again.__dict__


def decorator_func(wrapped):
    print 'decorating: ', wrapped.__name__

    wrapped.bar = 'bar'

    @functools.wraps(wrapped)
    def wrapper(*args, **kwargs):
        print 'before call wrapped: ', wrapped.__name__
        result = wrapped(*args, **kwargs)
        print 'after call wrapped: ', wrapped.__name__
        return result

    return wrapper
    # return functools.update_wrapper(wrapper, wrapped)


@decorator_func
def func(a, b):
    """func doc"""
    print a + b

print func.__name__
print func.__dict__
func('x', 'y')

