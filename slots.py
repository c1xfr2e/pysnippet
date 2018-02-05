
class Foo(object):
    _A = 'Foo_A'
    __B = '__FooB'


f = Foo()
print(f._A)
f._A = 'another Foo_A'
print(f._A)

print(f._Foo__B)


class C(object):
    __slots__ = ('__foo__', '__bar__')

    def __init__(self, x):
        object.__setattr__(self, '__foo__', x)
        object.__setattr__(self, '__bar__', 'class_C')

    def fun(self):
        print('C::fun()')


print(C.__dict__)

c = C('hello')
print(c.__foo__)
print(c.__bar__)

c.aaa = 'aaa'
