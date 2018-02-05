
class A(object):
    attr = 'A'


class B(object):
    attr = 'B'


class C(A, B):
    pass

print(C.attr)
C.attr = 'Now'

print(C.__bases__[0].attr)
print(C.__bases__[1].attr)


