### [Iterables vs. Iterators vs. Generators by Vincent Driessen](http://nvie.com/posts/iterators-vs-generators/)
![iter_gen explanation image](/images/iter_gen.png)
* **Iterables:** Most containers are also iterable. But many more things are iterable as well. Examples are open files, open sockets, etc. Where containers are typically finite, an iterable may just as well represent an infinite source of data.</br></br>
An iterable is any object, not necessarily a data structure, that can return an iterator (i.e., it has `__iter__()` method.). That sounds a bit awkward, but there is an important difference between an iterable and an iterator. Take a look at this example:</br>
```python
x = [1, 2, 3] # Iterable object
y = iter(x)   # Instance of an iterator
z = iter(x)   # Instance of an iterator
next(y)       # >>> 1
next(y)       # >>> 2
next(z)       # >>> 1
type(x)       # >>> <class 'list'>
type(y)       # >>> <class 'list_iterator'>
y1 = iter(x)
y2 = iter(y1)
print y1 is y2  # >>> True
                  # container.__iter__().__iter__() returns container.__iter__()
```

How for-loop works by Vincent Driessen
![for-loop explanation](/images/for_loop_explanation.png)

* **Iterators:**  Any object that has a `__next__()` method is therefore an iterator.
```python
''' infinite sequences '''
from itertools import count
counter = count(start=13)
next(counter)   # >>> 13
next(counter)   # >>> 14
''' finite sequences '''
from itertools import cycle
colors = cycle(['red', 'blue'])
next(colors)    # >>> 'red'
next(colors)    # >>> 'blue'
next(colors)    # >>> 'red'
from itertools import islice
colors = cycle(['red', 'white', 'blue'])  # infinite
limited = islice(colors, 0, 4)            # finite
for x in limited:                         # so safe to use for-loop on
  print(x)
    # >>> red, white, blue, red, .....
```
Both an iterable(has `__iter__()`) and iterator(has `__next__()`):
```python
class fib:
 def __init__(self):
    self.prev = 0
    self.curr = 1
 def __iter__(self):
    return self
 def __next__(self):
    value = self.curr
    self.curr += self.prev
    self.prev = value
    return value
f = fib()
print list(islice(f, 0, 10))
# >>> [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```


### [container.\__iter__() vs. iterator.\__iter__() *from* Stackoverflow](http://stackoverflow.com/questions/8125930/what-is-the-differences-between-container-iter-and-iterator-iter)

An iterator has an `__iter__()` method so that you can call iter() on it to get an iterator for it, even though it already is one. Makes it easier to write things that use iterators if you don't have to be constantly checking whether something is already an iterator or not.

So you're getting an iterator for the list, and then getting an iterator for that iterator. An iterator for an iterator is the original iterator (Python doesn't create a second iterator, there's no point).

OK, good so far.

Iterators are objects and, like all objects, have a lifecycle. They are created when you call `__iter__()` (or iter()) on the object and destroyed when there are no longer any references to them. In your example, you do a.`__iter__()`, which creates the list iterator. Then, since you don't keep a reference to the it anywhere, this iterator is destroyed more or less immediately (though this is an implementation detail). So your next command, a.`__iter__()`.`__iter__()` creates a new iterator for the list (only one, because the iterator of an iterator is the same iterator) -- it does not reuse the iterator you made in the previous command, because that iterator is gone. This is why the objects have different IDs; they are in fact different objects.

You will see that a.`__iter__()` and a.`__iter__()`.`__iter__()` are the same object if you keep a reference to the former. Try this:

```python
a = ['a', 'b', 'c']
i = iter(a)    # a.__iter__()
j = iter(i)    # i.__iter__() which is a.__iter__().__iter__()
print i is j   # True, they're the same object
```
