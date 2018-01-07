__author__ = 'zh'

def do():
    a = 1
    b = 2
    c = 0
    d = c or b or a
    print(d)
    d = a or b or c
    print(d)

import sys
print(sys.path)
