__author__ = 'zh'

def fun(first, default=None, *args, **kwargs):
    print('first', first)
    print('default', default)
    print(args)
    print(kwargs)

fun('first', ('127.0.0.1', 10000))