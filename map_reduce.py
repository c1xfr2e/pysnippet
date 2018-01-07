from functools import reduce

A = [1, 2, 3]
B = [4, 5, 6]

print(list(map(lambda x,y: x + y, A, B)))

print(reduce(lambda x,y: x+y, A))
