# coding=utf-8

import inspect

frame = None


def add(x, y):
    global frame
    s = x + y
    frame = inspect.currentframe()
    return s


add(2, 3)

print("Frame", frame)
print("Locals", frame.f_locals)
