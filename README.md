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

#### [Mutation]("http://book.pythontips.com/en/latest/mutation.html")

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

#### [\__slots__]("http://tech.oyster.com/save-ram-with-python-slots/")

By default Python uses a dict to store an object’s instance attributes. Which is usually fine, and it allows fully dynamic things like setting arbitrary new attributes at runtime.

However, for small classes that have a few fixed attributes known at “compile time”, the dict is a waste of RAM, and this makes a real difference when you’re creating a million of them. You can tell Python not to use a dict, and only allocate space for a fixed set of attributes, by settings \__slots__ on the class to a fixed list of attribute names:

**Warning:** Don’t prematurely optimize and use this everywhere! It’s not great for code maintenance, and it really only saves you when you have thousands of instances.
```python
class Image(object):
    __slots__ = ['id', 'caption', 'url']

    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url
        self._setup()

    # ... other methods ...
```


#### []("")
```python
```


#### []("")
```python
```
