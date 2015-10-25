#### [__repr__](http://chimera.labs.oreilly.com/books/1230000000393/ch08.html#_problem_119)
```python
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
p           # Pair(3, 4), __repr__() output
print(p)    # (3, 4), __str__() output

p = Pair(3, 4)
print('p is {0!r}'.format(p))   # p is Pair(3, 4)
print('p is {0}'.format(p))     # p is (3, 4)
'''It is standard practice for the output of __repr__()
to produce text such that eval(repr(x)) == x.'''
```
The use of format() in the solution might look a little funny, but the format code {0.x} specifies the x-attribute of argument 0. So, in the following function, the 0 is actually the instance self:

```python
def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)
# Or
def __repr__(self):
    return 'Pair(%r, %r)' % (self.x, self.y)
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
