# [O'reily Cookbook](http://chimera.labs.oreilly.com/books/1230000000393/ch01.html#_problem_2)

### Unpacking Elements from Iterables of Arbitrary Length
```python
def read_transcripts(transcript):
    name, department, *grades = transcript
    return sum(grades) / float(len(grades))

print(read_transcripts(["Seyoung", "CS", 5, 4, 5, 3, 5]))       # 4.4
```

```python
records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
```

```python
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)       # ACME 2012
```

#### Interesting recursive unpacking
```python
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
```

### Deque, generator, files
```python
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('python_text.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
```

### collections.deque
```python
q = deque()
q.append(1)
q.append(2)
q.append(3)         # deque([1, 2, 3])
q.appendleft(4)     # deque([4, 1, 2, 3])
q.pop()     # 3     # deque([4, 1, 2])
q.popleft() # 4
```
Adding or popping items from either end of a queue has O(1) complexity. This is unlike a list where inserting or removing items from the front of the list is O(N).

### Unpacking Elements from Iterables of Arbitrary Length
```python

```

### Unpacking Elements from Iterables of Arbitrary Length
```python

```

### Unpacking Elements from Iterables of Arbitrary Length
```python

```

### Unpacking Elements from Iterables of Arbitrary Length
```python

```
