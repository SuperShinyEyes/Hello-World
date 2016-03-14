//: Playground - noun: a place where people can play

import UIKit



class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}



var john: Person = Person(name: "John Appleseed")
var unit4A: Apartment?

unit4A = Apartment(unit: "4A")


john.apartment = unit4A
unit4A!.tenant = john


var soundDictionary:[String:String] = ["cow":"moo", "dog":"bark", "pig":"squeal"]
print(soundDictionary["cow"]) // prints moo
print(soundDictionary["fox"]) // what does the fox say?
print(Optional(1) == 1)

var no: Int
//print(no)
//no == nil
no = 10
no == 10
print(no)

var list = ["hello", "world"]
list.joinWithSeparator(".")
var slice: Array<String> = Array(list[0..<1])
list.contains("hello")
list.contains("hell")

var listCopy = list
listCopy.removeAll()
print(list, listCopy)
var five = 5
var fiveCopy = five
five += 1
print(five, fiveCopy)
list += ["kk"]
print(list)

var a = [1,2,3]
a += (4...10)
print(a)
a.replaceRange((1...3), with: (4...10))
var b = a.sort {$0 > $1}
print(b)
print(a)
a.sort()
var c = a.filter {$0 % 2 == 0}
print(c)
var r = c.reduce(0) {$0 + $1}
print(r)

var hello = "hello"

let index = hello.startIndex.advancedBy(3)
hello.substringFromIndex(index)
hello.substringWithRange(Range<String.Index>(start: hello.startIndex.advancedBy(0), end: hello.endIndex.advancedBy(-3)))
hello.appendContentsOf("koko")
hello.capitalizedString
hello.insertContentsOf("koko".characters, at: hello.startIndex.advancedBy(3))
