
pkg_str = 'pkg_foo.foo.s'
module_name, obj_name = pkg_str.rsplit('.', 1)

m = __import__(module_name, None, None, [obj_name, 'fun'])
m.fun()

import pkg_foo

print(dir(pkg_foo))

pkg_foo.fun()

pkg_foo.foo.fun()
pkg_foo.bar.fun()
