# coding=utf8


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0

    def gratuitous_refactor():
        name = "gratuitous"
        print(name[::-1])
        nonlocal index
        while index < up_to:
            yield index
            index += 1
        return 1000

    gr = gratuitous_refactor()
    yield_from = yield from gr

    # Get here when gr ends with StopIteration
    print("yield from gratuitous_refactor", yield_from)


r = lazy_range(3)
print(next(r))
print(next(r))
print(next(r))


def bottom():
    # Returning the yield lets the value that goes up the call stack to come right back
    # down.
    name = "bottom"
    print("--------bottom")
    b = (yield 42)
    print("--------bottom#")
    return b


def middle():
    name = "middle"
    print("----middle")
    b = bottom()
    m = yield from b
    print("----middle#")
    return m


def top():
    name = "top"
    print("top")
    t = (yield from middle())
    print("top#")
    return t


# Get the generator.
gen = top()
value = next(gen)
print(value)
try:
    value = gen.send(value * 2)
except StopIteration as exc:
    value = exc.value
print(value)