# coding=utf-8

A = [1, 3, 5, 7, 3, 2, 6, 9, 0, 8, 1, 4, 6, 3]
d = {}
for i in A:
    d[i] = d.get(i, 0) + 1

print(d)
print(list(filter(lambda x: d[x] > 1, d)))

for k in d.items():
    print(k)
