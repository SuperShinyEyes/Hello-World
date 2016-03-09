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