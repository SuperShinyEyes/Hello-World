from datetime import datetime

class Person(object):
  """ It's a frame for human objects """
  def __init__(self, name, birthday, sex):
    self.name = name
    self.birthday = birthday
    self.age = self.get_age()
    self.sex = sex

  # Class method
  def set_birthday(self):
    format = '%Y/%m/%d'
    self.birthday = datetime.strptime(self.birthday, format)

  # Class method
  def get_age(self):
    self.set_birthday()
    today = datetime.today()
    return (today - self.birthday).days / 365

  def __str__(self):
    sentence = "My name is %s. I'm %d years old and %s." % (self.name, self.age, self.sex)
    return sentence

seyoung = Person('Seyoung', '1990/02/16', 'male')
print seyoung.age
print seyoung.birthday
print seyoung
print Person.__doc__
