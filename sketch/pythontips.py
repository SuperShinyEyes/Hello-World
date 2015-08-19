g = (i for i in range(5))
print type(g)
for i in g:
  print i

def get_g():
  for i in range(5):
    yield i

a = get_g()
print a.next()
# print len(a)
print type(a)
print a.next()
print next(a)
l = range(5)
print iter(l)
print l.__iter__()

print next(iter(l))

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

y = yrange(5)
y2 = yrange(5)
print y.__iter__() is y
print y.__iter__() is y2

class reverse_iter(object):
  """docstring for """
  def __init__(self, l):
    self.l = l
    self.i = len(l) - 1

  def __iter__(self):
    return self

  def next(self):
    if self.i >= 0:
      i = self.i
      self.i -= 1
      return self.l[i]
    else:
      raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

print sum(x*x for x in range(10))
x = xrange(10)
print type(x)
print range(10)
xrange

def file_generator(filename):
  with open(filename) as f:
    for line in f:
      if line != '\n':
        yield line

def cat(filenames):
  for filename in filenames:
    for line in file_generator(filename):
      print line

cat(['/Users/young/projects/Hello Python/README.md'])

import itertools
it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
c = itertools.chain(it2, it1)
print list(c)

for x, y in itertools.izip(["a", "b", "c", "d"], [1, 2, 3]):
 print x, y

def peep(iterator):
  first = [next(iterator)]
  iterator = itertools.chain(iter(first), iterator)
  return first, iterator
  #
first, it1 = peep(iter([1, 2, 3]))
for i in it1:
  print i

d = {1:1, 0:2, 3:3}
for k, v in enumerate(d):
  print k, v

def my_enumerate(iterable):
  return ((i, iterable[i]) for i in xrange(len(iterable)))

l = [3,4,5,6,7]
print l.__iter__()

t = (1,2,3)
print type(t), t.__iter__()
e = my_enumerate(l)

for i, v in e:
  print i, v

def izip(it1, it2):
  length = min(len(it1), len(it2))
  return ((it1[i], it2[i]) for i in xrange(length))

print list(izip([2,30,5,7],[4,5,6]))

x = [1, 2, 3]
y1 = iter(x)
print y1.next()
y2 = iter(y1)
print y1 is y2
