# Minheap algorithm benchmark: Generator vs. Non-generator

### Introduction
The idea comes from one of the course assignments at Aalto, Data Structure and Algorithms.
An assistant, Riikka, suggested me using a generator for getting parent nodes in a heap tree.

### Benchmark test result
I ran a benchmark test with 150 000 inputs.

Generator | Non-generator
----------|--------------
2.98 sec | 1.52 sec
*Benchmark test with 150,000 inputs*

### Codes
#### Generator
```python
def parent(i):
    while i > 1:
        i //= 2
        yield i

def _heapify_up(i):
    arr = list(range(10))
    min_child = i
    if arr[min_child] < arr[i]:
        arr[min_child], arr[i] = arr[i], arr[min_child]


def insert_generator(obj):
    z = 1
    for p in parent(z):
        heapify_up(p)
    return obj
```

#### Non-generator
```python
def _heapify_up2(child_index):
    arr = list(range(10))
    parent_index = child_index // 2
    while parent_index > 0 and arr[child_index] < arr[parent_index]:
        arr[child_index], arr[parent_index] = arr[parent_index], arr[child_index]
        parent_index, child_index = parent_index // 2, parent_index


def insert_non_generator( obj):
    z = 1
    _heapify_up2(z)
    return obj
```

### Disassembly
Use [*dis*](https://docs.python.org/2/library/dis.html)
```python
import dis

dis.dis(insert_generator)

'''
2           0 LOAD_CONST               1 (1)
              3 STORE_FAST               1 (z)

  3           6 SETUP_LOOP              30 (to 39)
              9 LOAD_GLOBAL              0 (parent)
             12 LOAD_FAST                1 (z)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 GET_ITER
        >>   19 FOR_ITER                16 (to 38)
             22 STORE_FAST               2 (p)

  4          25 LOAD_GLOBAL              1 (heapify_up)
             28 LOAD_FAST                2 (p)
             31 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             34 POP_TOP
             35 JUMP_ABSOLUTE           19
        >>   38 POP_BLOCK

  5     >>   39 LOAD_FAST                0 (obj)
             42 RETURN_VALUE
'''
```

```python
dis.dis(insert_non_generator)

'''
2           0 LOAD_CONST               1 (1)
              3 STORE_FAST               1 (z)

  3           6 LOAD_GLOBAL              0 (_heapify_up2)
              9 LOAD_FAST                1 (z)
             12 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             15 POP_TOP

  4          16 LOAD_FAST                0 (obj)
             19 RETURN_VALUE
'''
```

### Conclusion
Wouldn't really did into what the dis results mean line by line at midnight. However, the generator version seems more complicated than the other one obviously.
