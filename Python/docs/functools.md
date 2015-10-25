## [partial](http://www.pydanny.com/python-partials-are-fun.html)
What functools.partial does is:<br>
* Makes a new version of a function with one or more arguments already filled in.
* New version of a function documents itself.

```python
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
```
Partial also creates a *documentation* itself.
```python
assert square.keywords == {"exponent": 2}
assert square.func == power

assert cube.keywords == {"exponent": 3}
assert cube.func == power
```
To organize using class
```python
# Since I like my article code to work in both Python 2.7 and 3,
#   I'll import the excellent six library to manage the
#   differences between Python versions. Six is available on PyPI
#   at https://pypi.python.org/pypi/six.
from six import add_metaclass

class PowerMeta(type):
    def __init__(cls, name, bases, dct):

        # generate 50 partial power functions:
        for x in range(1, 51):

            # Set the partials to the class
            setattr(
                # cls represents the class
                cls,

                # name the partial
                "p{}".format(x),

                # partials created here
                partial(power, exponent=x)
            )
        super(PowerMeta, cls).__init__(name, bases, dct)

@add_metaclass(PowerMeta)
class PowerStructure(object):
    pass
```
Let's test it.
```python
def test_power_structure_object():
    p = PowerStructure()

    # 10 squared
    assert p.p2(10) == 100

    # 2 to the 5th power
    assert p.p5(2) == 32

    # 2 to the 50th power
    assert p.p50(2) == 1125899906842624
```
And you don't even need to instantiate.
```python
def test_power_structure_class():
    # Thanks to the power of metaclasses, we don't need to instantiate!

    # 10 squared
    assert PowerStructure.p2(10) == 100

    # 2 to the 5th power
    assert PowerStructure.p5(2) == 32

    # 2 to the 50th power
    assert PowerStructure.p50(2) == 1125899906842624
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

## example
```python
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

## example
```python
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

## example
```python
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

## example
```python
```
