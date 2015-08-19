#### [nvie](http://nvie.com/posts/use-more-iterators/)

```python
filename = "README.md"

def get_lines(filename):
  with open(filename) as f:
    for line in f:
      if not line.startswith('#'):
        yield line

lines_list = list(get_lines(filename))
lines_set = set(get_lines(filename))
lines_tuple = tuple(get_lines(filename))

longest_line = max(get_lines(filename), key=len)
print longest_line
longest_line = max(get_lines(filename), key=lambda x:len(x))
print longest_line
```
Get the first 10 lines
```python
from itertools import islice
first_ten_lines = list(islice(get_lines(filename), 0, 10))
```
