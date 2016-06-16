
class A(object):
    attr = 'A'


class B(object):
    attr = 'B'


class C(A, B):
    pass

print C.__bases__[1].attr


