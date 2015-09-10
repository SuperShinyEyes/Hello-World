## Modifying a dict while looping over it
The follwing will throw a RuntimeError.
```python
d = {'matt': 'blue', 'rachel':'green', 'ray':'red'}
for k in d:
    if k.startswith('r'):
        del d[k]
```
The following doesn't because it first makes a duplicate.
```python
for k in d.keys():
    if k.startswith('r'):
        del d[k]

print d
```

## Get keys and values from a dict
```python
d.items()       # Returns a list of tuples
d.iteritems()   # Returns an iterator of tuples
```

## Construct a dict from pairs
```python
from itertools import izip
names = ['sean', 'sam', 'sandy']
colors = ['red', 'green', 'blue', 'yellow']
print dict(izip(names, colors))
# Returns {'sandy': 'blue', 'sean': 'red', 'sam': 'green'}
```

## Construct a dict from sequence with its indices
```python
print dict(enumerate(names))
```

## Counting in a sequence
```python
colors = ['red', 'green', 'blue', 'yellow', 'red', 'green', 'red']
from collections import Counter
print Counter(colors)
# Counter({'red': 3, 'green': 2, 'blue': 1, 'yellow': 1})
```

## [Counting in a sequence with get()](https://docs.python.org/2/library/stdtypes.html#dict.get)

**get(key[, default])**<br>
Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
```python
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
```

## [collections.defaultdict](http://book.pythontips.com/en/latest/collections.html#defaultdict)
```python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
```
Another use case like json tree:
```python
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
# Works fine

import json
print(json.dumps(some_dict))
# Output: {"colours": {"favourite": "yellow"}}
```

## [collections.Counter](http://book.pythontips.com/en/latest/collections.html#counter)
```python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)
# Output: Counter({
#    'Yasoob': 2,
#    'Ali': 2,
#    'Arham': 1,
#    'Ahmed': 1
# })
```

```python
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)

max_value = 0
for k, v in line_count.iteritems():
  if v > max_value:
    max_value = v
    max_pair = {k, v}

print max_pair
```

## [collections.deque](http://book.pythontips.com/en/latest/collections.html#deque)
```python
from collections import deque

d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: 0

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])
```
set maxlen
```python
d = deque(maxlen=30)
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)      # Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```
## [collections.namedtuple]()
```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)             # Output: Animal(name='perry', age=31, type='cat')
print(perry.name)        # Output: 'perry'
print(perry[0])          # Output: 'perry'
print(perry._asdict())   # Output: OrderedDict([('name', 'perry'), ('age', 31), ...
```
## dict.popitems()
```python
d = {'matt': 'blue', 'rachel':'green', 'ray':'red'}
while d:
    k, v = d.popitem()
    print k, v
```

## example
```python
```

## example
```python
```

## example
```python
```
