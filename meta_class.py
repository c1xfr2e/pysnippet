
def fun(self):
    print 'fun()', self.name


Foo = type(
    'Foo',
    (object,),
    {
        'name': 'class_Foo',
        'fun': fun
    }
)
print Foo
print Foo.__dict__


foo_1 = Foo()
print foo_1.__dict__

print Foo.fun
print foo_1.fun

foo_1.fun()


class Meta(type):
    def __new__(cls, name, bases, attrs):
        return super(Meta, cls).__new__(cls, name, bases, attrs)

    def __init__(cls, *args, **kwargs):
        type.__init__(cls, *args, **kwargs)
        print 'Meta::__init__', cls.__name__
        cls._unbound_fields = {}

    def __call__(cls, *args, **kwargs):
        print 'Meta::__call__', cls.__name__
        return type.__call__(cls, *args, **kwargs)

    def function_in_meta(cls):
        pass


print 'Meta: ', Meta, type(Meta)

meta_i_1 = Meta('Meta_1', (object,), {})
meta_i_2 = Meta('Meta_2', (object,), {})


class Bar(meta_i_1):
    a = 'a'
    x = 'x'

    def __new__(cls, *args, **kwargs):
        return super(Bar, cls).__new__(cls)
    
    def __init__(self, *args, **kwargs):
        super(Bar, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print 'Bar::__call__', Bar.a, Bar.x


class Baz(Meta('Meta', (object,), {})):
    def __init__(self):
        print 'Baz::__init__'
        super(Baz, self).__init__()

print issubclass(int, int)
print issubclass(Foo, Foo)
print issubclass(Bar, Bar)
print isinstance(Bar, Bar)

bar = Bar()
print bar
bar()

# Can not find attribute in meta class.
# bar.function_in_meta()

class C(object):
    def __init__(self, a):
        self.a = a

c = object.__new__(C)
c.__init__('c1')
print c.a

c2 = type.__call__(C, 'c2')
print c2.a

#####################################################################

def make_hook(f):
    """Decorator to turn 'foo' method into '__foo__'"""
    f.is_hook = 1
    return f

class MyType(type):
    def __new__(cls, name, bases, attrs):

        if name.startswith('None'):
            return None

        # Go over attributes and see if they should be renamed.
        newattrs = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue

        return super(MyType, cls).__new__(cls, name, bases, newattrs)

    def __init__(self, name, bases, attrs):
        super(MyType, self).__init__(name, bases, attrs)

        # classregistry.register(self, self.interfaces)
        print "Would register class %s now." % self

    def __add__(self, other):
        class AutoClass(self, other):
            pass
        return AutoClass
        # Alternatively, to autogenerate the classname as well as the class:
        # return type(self.__name__ + other.__name__, (self, other), {})

    def unregister(self):
        # classregistry.unregister(self)
        print "Would unregister class %s now." % self

class MyObject:
    __metaclass__ = MyType

    def f(self):
        pass


class NoneSample(MyObject):
    pass

# Will print "NoneType None"
print type(NoneSample), repr(NoneSample)

class Example(MyObject):
    def __init__(self, value):
        self.value = value
    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)

# Will unregister the class
Example.unregister()

inst = Example(10)
# Will fail with an AttributeError
#inst.unregister()

print inst + inst
class Sibling(MyObject):
    pass

ExampleSibling = Example + Sibling
# ExampleSibling is now a subclass of both Example and Sibling (with no
# content of its own) although it will believe it's called 'AutoClass'
print ExampleSibling
print ExampleSibling.__mro__
