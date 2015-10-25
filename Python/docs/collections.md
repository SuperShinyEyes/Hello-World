#### Looping over two collections
```python
names = ['sean', 'sam', 'sandy']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print "{n} likes {c}".format(n=name, c=color)
```
However zip() will create a list and that's not memory efficient.<br>
[itertools.izip() creates an iterator.](https://docs.python.org/2/library/itertools.html#itertools.izip)
```python
def izip(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))
```
Hence, the above code could be improved as following:
```python
import itertools
for name, color in itertools.izip(names, colors):
    print "{n} likes {c}".format(n=name, c=color)

```

#### Call a function until a sentinel(last) value
```python
import functools
blocks = []
with open("README.md") as f:
    for block in iter(functools.partial(f.read, 32), ''):
        blocks.append(block)
print blocks

```

#### example
```python
```

#### example
```python
```

#### example
```python
```

#### example
```python
```

#### example
```python
```

#### example
```python
```
