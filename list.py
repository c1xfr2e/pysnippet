from functools import reduce
def sum(seq, start=0):
    def add(x,y): return x+y
    return reduce(add, seq, start)
print(list(range(1, 6)))
print(sum(list(range(1, 6)), 0))
print(sum(list(range(1, 6)), 100))
print(sum(list(range(1, 6)), 2))