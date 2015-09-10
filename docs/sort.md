### [wiki.python](https://wiki.python.org/moin/HowTo/Sorting)
#### sorted() - Returns the item sorted.
sorted() takes any iterable.
```python
sorted([5, 2, 3, 1, 4])     # [1, 2, 3, 4, 5]
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
# [1, 2, 3, 4, 5]
```

#### list.sort() - Sort the item in-place. Returns None.
```python
a = [5, 2, 3, 1, 4]
a.sort(cmp=None, key=None, reverse=False)
print a     # [1, 2, 3, 4, 5]
```

#### sorted()/list.sort() *key* parameter
```python
sorted("Today is a sunny day as Sam longed for".split(), key=str.lower)
# ['a', 'as', 'day', 'for', 'is', 'longed', 'Sam', 'sunny', 'Today']
```
```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
```python
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)   # sort by age
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

#### example
```python
```

#### example
```python
```
