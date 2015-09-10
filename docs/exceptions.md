#### [Different ways to handle](http://book.pythontips.com/en/latest/exceptions.html)
```python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```
```python
try:
    file = open('test.txt', 'rb')
except Exception:
    # Some logging if you want
    raise
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

#### example
```python
```

#### example
```python
```

#### example
```python
```
