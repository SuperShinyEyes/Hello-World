# a = range(10)
# print a
# a.sort(reverse=True)
# print a
# print sorted(a)
# print a
# print sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
# print "This is a test string from Andrew".split()
# print sorted("Today is a sunny day as Sam longed for".split(), key=str.lower)
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# print sorted(student_tuples, key=lambda student: student[2])
#
# class Student:
#     def __init__(self, name, grade, age):
#         self.name = name
#         self.grade = grade
#         self.age = age
#
#     def __repr__(self):
#         return repr((self.name, self.grade, self.age))
#
# student_objects = [
#     Student('john', 'A', 15),
#     Student('jane', 'B', 12),
#     Student('dave', 'B', 10),
# ]
#
# print student_objects[0].__repr__()
# print sorted(student_objects, key=lambda student: student.age)   # sort by age


class Pair:
    def __init__(self, x, y):
    self.x = x
    self.y = y
    def __repr__(self):
    return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
    return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
print p
