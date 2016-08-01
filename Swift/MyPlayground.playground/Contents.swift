//: Playground - noun: a place where people can play

import UIKit


class Car {
    init(){
        print("init")
    }
    
    deinit {
        print("done")
    }
}

var a: Car? = Car()
a = nil

func appendToArray(inout a: [Int], b: Int) {
    a.append(b)
}

//var b: [[Int]] = (0...10).map { i -> [Int] in return [i, 10] }
var b1 = 1
var b2 = [b1]
var b = [b2]
//var c: [[Int]] = b.map { (inout i: [Int]) -> [Int] in
//    i.append(10)
//    return i
//    //    return appendToArray(i, b: 11)
//}


(0...10).map {(i:Int) -> Int in var temp = i; temp += 1; return temp}
struct Stack<Element> {
    var items = [Element]()
    mutating func push(item: Element) {
        items.append(item)
    }
    mutating func pop() -> Element {
        return items.removeLast()
    }
}

var s = Stack<Int>()
s.push(1)
s.pop()