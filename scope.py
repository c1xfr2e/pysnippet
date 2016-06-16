__author__ = 'zh'

for i in range(0, 10):
    if i == 0:
        L = []
    else:
        L.append(i)

print i
print L

d = (x * y for x in range(0, 3) for y in range(1,3))
# print x
print list(d)

def fun():
    # print x
    x = 100
    print x

fun()
