# Python main cheat sheet
#### [Ternary Operators](http://book.pythontips.com/en/latest/ternary_operators.html)
```python
is_fat = True
state = "fat" if is_fat else "not fat"
```

#### [set](http://book.pythontips.com/en/latest/ternary_operators.html)
```python
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
# Output: set(['b', 'n'])

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input = set(['red', 'brown'])
print(input.intersection(valid))
# Output: set(['red'])
print(input.difference(valid))
# Output: set(['brown'])
```

#### [Decorators](http://book.pythontips.com/en/latest/decorators.html)
```python
from datetime import datetime
from functools import wraps

def timed(func):
  ''' Benchmarking wrapper
  @wraps preserves the pre-decorated function's property.
  e.g., some_func.__name__ will return "some_func" not "decorated" '''
  @wraps(func)
  def decorated(*args, **kwargs):
    pre_t = datetime.utcnow()
    result = func(*args, **kwargs)
    post_t = datetime.utcnow()
    duration = (post_t - pre_t).total_seconds()
    print "\t%s: %.2f sec" % (func, duration)
    return result
  return decorated

@timed
def some_func():
  pass
```

#### [Mutation](http://book.pythontips.com/en/latest/mutation.html)
Whenever you assign a variable to another variable of mutable datatype, any changes to the data are reflected by both variables. The new variable is just an alias for the old variable. This is only true for mutable datatypes
```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]
```
 In Python the default arguments are evaluated once when the function is defined, not each time the function is called. You should never define default arguments of mutable type unless you know what you are doing. You should do something like this:
```python
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

```

#### [\__slots__](http://tech.oyster.com/save-ram-with-python-slots/)

By default Python uses a dict to store an object’s instance attributes. Which is usually fine, and it allows fully dynamic things like setting arbitrary new attributes at runtime.

However, for small classes that have a few fixed attributes known at “compile time”, the dict is a waste of RAM, and this makes a real difference when you’re creating a million of them. You can tell Python not to use a dict, and only allocate space for a fixed set of attributes, by settings \__slots__ on the class to a fixed list of attribute names:

```python
class Image(object):
    __slots__ = ['id', 'caption', 'url']

    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url
        self._setup()

    # ... other methods ...
cat = Image(1, "cat", "path/to/cat")
cat.url = "new_path/to/cat"   # Works fine
cat.age = 1                   # Raise an AttributeError
cat.__dict__                  # Raise an AttributeError
```
**Warning:** Don’t prematurely optimize and use this everywhere! It’s not great for code maintenance, and it really only saves you when you have thousands of instances. This only runs on [new style classes](http://stackoverflow.com/a/54873/3067013).

**Tip:** [PyPy](http://pypy.org/) automatically does \__slots__ and other optimization

#### [collections.defaultdict](http://book.pythontips.com/en/latest/collections.html#defaultdict)
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

#### [collections.Counter](http://book.pythontips.com/en/latest/collections.html#counter)
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

#### [collections.deque](http://book.pythontips.com/en/latest/collections.html#deque)
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
#### [collections.namedtuple]()
```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)             # Output: Animal(name='perry', age=31, type='cat')
print(perry.name)        # Output: 'perry'
print(perry[0])          # Output: 'perry'
print(perry._asdict())   # Output: OrderedDict([('name', 'perry'), ('age', 31), ...
```

#### [enumerate](http://book.pythontips.com/en/latest/enumerate.html)
```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
```

#### Get Bluetooth Mac addresses
```python
import bluetooth
nearby_devices = bluetooth.discover_devices()
for mac_address in nearby_devices:
  print mac_address
```

#### Write object to a file
```python
import pickle

with open(filename, 'wb') as f:
  pickle.dump(nearby_devices, f)

if os.path.isfile(filename):
  print "read list"
  with open(filename, 'rb') as f:
    existing_bt_list = pickle.load(f)
```

#### example
```python
```

#### example
```python
```
