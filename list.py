def sum(seq, start=0):
    def add(x,y): return x+y
    return reduce(add, seq, start)
print range(1, 6)
print sum(range(1, 6), 0)
print sum(range(1, 6), 100)
print sum(range(1, 6), 2)