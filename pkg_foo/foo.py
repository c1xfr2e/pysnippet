
print 'in pkg_foo/foo.py'

def fun():
    print 'in pkg_foo.foo.fun'
    return 'pkg_foo/foo.py/fun()'

s = fun()

print 'out pkg_foo/foo.py'
