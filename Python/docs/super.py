#!/usr/bin/env python3

'''
Exercise from "Raymond Hettinger - Super considered super! - PyCon 2015 "
https://www.youtube.com/watch?v=EiOglTERPEo
Error code example: pastebin(doc)com/jC9nd0S0
'''

class Adam(object): pass
class Eve(object): pass
class Adam2(object): pass
class Eve2(object): pass
class Ramon(Adam, Eve): pass
class Gayle(Adam, Eve): pass
class Raymond(Ramon, Gayle): pass
class Dennis(Adam, Eve): pass
class Sharon(Adam, Eve): pass
class Rachel(Dennis, Sharon): pass
class Matthew(Raymond, Rachel): pass

help(Matthew)

'''
Result:

class Matthew(Raymond, Rachel)
 |  Method resolution order:
 |      Matthew
 |      Raymond
 |      Ramon
 |      Gayle
 |      Rachel
 |      Dennis
 |      Sharon
 |      Adam
 |      Eve
 |      __builtin__.object
 |
 |  Data descriptors inherited from Adam:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 '''

# Super() is equal to "Next in line "

class DoughFactory(object):
    def get_dough(self):
        return "insecticide treated wheat dough"

class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print("Getting dough")
        # dough = DoughFactory().get_dough()
        dough = super().get_dough()
        print("Making pie with %s" % dough)
        for topping in toppings:
            print("Adding: %s" % topping)

Pizza().order_pizza("pepperoni", 'Bell Pepper')

class Robot(object):
    def fetch(self, tool):
        print("Physical Movement! Fetching")
    def move_forward(self, tool):
        print("Physical Movement! Moving forward")
    def move_backward(self, tool):
        print("Physical Movement! Moving backward")
    def replace(self, tool):
        print("Physical Movement! Replacing")

class CleaningRobot(Robot):
    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)

cleaner = CleaningRobot()
cleaner.clean("broom")

class MockBot(Robot):

    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)


from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter("abbaslkjgsioasfd;lkj")
print(oc)

super() was designed for multiple cooperative inheritance

stopper class
