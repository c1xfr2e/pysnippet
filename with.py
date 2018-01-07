
f = open('with.py', 'r')
f.__enter__
f.__exit__


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('__enter__')
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with Foo('foo') as foo:
    print(foo)
    raise Exception()
    print('exit with')
