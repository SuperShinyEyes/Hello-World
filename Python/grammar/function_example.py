from sets import Set

''' Simple computation '''
print 1 + 1
print "Hello world!"
print "1 + 1 is equal to %d :)" % 2

'''
Variables
Binding values to human readable "names" make things very easy.
'''
Eugene = 13
print Eugene
Jiwon = 16
myname = "Seyoung"
print Eugene + Jiwon
print myname + Eugene
print myname
print "Is Eugene order than Jiwon? ===> %r" % (Eugene > Jiwon)
Eugene_after_ten_years = Eugene + 10
print Eugene_after_ten_years


''' Datatypes '''
name = 'Seyoung'          # String
age = 25                  # Integer
height = 174.6            # Float
is_cool = True            # Boolean
food_he_ate = ["yogurt", "rice", "bulgogi", "rice", "soup"] # List
print food_he_ate
print food_he_ate[2]
food_he_ate.append("noodle")
food_he_ate.append("rice")
print food_he_ate
treasure = ("Heeryung", "watermelon", "nature") # Tuple

family = Set(["Dad", "Mom", "Sehyun"])            # Set
family.add("Mom")
print family

contact = {"cell":92097135, "home":9245010}     # Dictionary
print contact['home']
contact["girlfriend"] = 7118
print contact

''' List: Data basket with order and duplicates '''

''' function '''
def add(a, b):
  return a + b

print add(1, 1)
print add(10, 10)
print add(4, 6)

def subtract(a, b):
  return a - b

print subtract(1, 1)
print subtract(10, 10)
print subtract(4, 6)

def multiply(a,b):
  return a*b

print multiply(10,1000000)

def divide(a,b):
  return float(a)/b

print divide(22,7)

def geometric_sum(haha):
  result>1
  y=abs(haha)

b=(1,2,3,4,5,6,7,8,9,0.1,3.14159267)

def read_basket(basket):
  for i in basket:
    print i

def introduce(name, age, is_cool, food_he_ate, treasure, family, contact):
  sentence = "%s is %d years old. Is he cool? ===> %r." % (name, age, is_cool)
  print sentence

introduce(name, age, is_cool, food_he_ate, treasure, family, contact)

result = 1
y = 2
while y > 0:
  result *= y
  y -= 1
  print " y:%d, result:%d" % (y, result)


start = 0
order = 1
while order < 100:
  if start == 0:
    print "order: %d, value:%d" %(order, start)
    old = start
    start += 1
  else:
    new_start = start + old
    old = start
    start = new_start
    print "order: %d, value:%d" %(order, start)
  order += 1
