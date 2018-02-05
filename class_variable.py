# codeing: utf-8


class P(object):
    x = 1


class C1(P):
    pass


class C2(P):
    pass


print(P.x, C1.x, C2.x)
C1.x = 2
print(P.x, C1.x, C2.x)
P.x = 3
print(P.x, C1.x, C2.x)
C2.x = 100
print(P.x, C1.x, C2.x)
P.x = 300
print(P.x, C1.x, C2.x)
