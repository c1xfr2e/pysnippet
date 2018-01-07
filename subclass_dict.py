
from collections import defaultdict


class DefaultDict(dict):
    def __missing__(self, key):
      return ['__missing__']


d = DefaultDict()
d['florp'] = 127
print(d['foo'], d['bar'])

dftd = defaultdict(lambda: 0)
print(dftd.get('foo'))
print(dftd['bar'])
