__author__ = 'zh'


def make(L):
    def inner():
        print(L)
    return inner


L = [1, 2]
closure = make(L)
L.append('abc')
closure()
