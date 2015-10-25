d = {'matt': 'blue', 'rachel':'green', 'ray':'red'}

d.iteritems()
from itertools import izip
names = ['sean', 'sam', 'sandy']
colors = ['red', 'green', 'blue', 'yellow', 'red', 'green', 'red']


d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print d

d = {}
for color in colors:
    d[color] = d.setdefault(color, 0) + 1
print d

from collections import *
d = defaultdict(list)
for c in colors:
    d[len(c)].append(c)
print dict(d)

while d:
    k, v = d.popitem()
    print k, v
