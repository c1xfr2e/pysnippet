
class NonDataDesc(object):
    def __get__(self, instance, owner):
        pass

    '''
    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass
    '''


class DataDesc(object):
    def __get__(self, instance, owner):
        print(self, instance, owner)
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("can't set attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't write attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)


class StaticMethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        return self.func


def my_staticmethod(func):
    return StaticMethod(func)


class ClassMethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if cls is None:
            cls = type(instance)

        def newfunc(*args, **kwargs):
            return self.func(cls, *args, **kwargs)

        return newfunc


def my_classmethod(func):
    return ClassMethod(func)


class B(object):
    def __init__(self, k=None):
        self._k = k
        self._r = '_r'

    non_data_desc = NonDataDesc()
    data_desc = DataDesc()

    def getk(self):
        return self._k

    def setk(self, value):
        self._k = value    

    k = Property(getk, setk)

    @property
    def r(self):
        return self._r


b = B('kkk')
print(B.__dict__)
# override non-data descriptor
print(b.non_data_desc)
b.non_data_desc = "non_data_desc"
print(b.non_data_desc)
# override data descriptor
print(b.data_desc)
b.data_desc = "data desc"
print(b.data_desc)

print(b.k)
b.k = 'set k'
print(b.r)
# b.r = 'r'
# del b.r


class C(B):
    def __init__(self):
        super(C, self).__init__()
        self.x = 'B_x'
        self.y = 'B_y'

    @my_staticmethod
    def f_static(foo, bar):
        print(foo, bar)

    @my_classmethod
    def f_class(cls, foo):
        print(cls, foo)


c = C()
print(c.__dict__)
print(c.x)
print(c.k)
print(c.y)

c.f_static('123', 'abc')
C.f_static('snake', 'egg')

def f(self, foo):
    print(self, foo)

C.f_static = f
c.f_static('H')

C.f_class('by class')
c.f_class('by instance')
