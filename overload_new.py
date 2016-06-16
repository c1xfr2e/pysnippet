
class Foo(object):
    def __new__(cls, *args, **kwargs):
        origin = super(Foo, cls).__new__(cls)
        return origin
        return Bar(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print args, kwargs
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


class Bar(object):
    def __init__(self, the_class, *args, **kwargs):
        print 'init Bar object from', the_class
        self.the_class = the_class
        for k, v in kwargs.iteritems():
            setattr(self, k, v)


foo = Foo(name='foo_hello')
print foo.the_class.__name__, foo.name
