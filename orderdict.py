from collections import OrderedDict
import random


print("hello")
A = [random.randint(0,20) for i in range(0,8)]
od = OrderedDict((k, True) for k in A)
if 10 in od:
    print("OK")
