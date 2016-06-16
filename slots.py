
class Foo(object):
    _A = 'Foo_A'
    __B = '__FooB'


f = Foo()
print f._A
f._A = 'another Foo_A'
print f._A

print f._Foo__B


class C(object):
    __slots__ = ('__foo', '__bar__')

    def __init__(self, x):
        object.__setattr__(self, '_C__foo', x)
        object.__setattr__(self, '__bar__', 'class_C')

    def fun(self):
        print 'C::fun()'


print C.__dict__

c = C('hello')
print c._C__foo
print c.__bar__

c.a = 'a'
