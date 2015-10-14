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
class Dennis(Adam2, Eve): pass
class Sharon(Adam, Eve2): pass
class Rachel(Dennis, Sharon): pass
class Matthew(Raymond, Rachel): pass

help(Matthew)
