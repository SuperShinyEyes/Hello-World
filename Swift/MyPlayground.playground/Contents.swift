//: Playground - noun: a place where people can play

import UIKit


(0...10)


extension SequenceType {
    func count<U>(Element) -> Int {
        var result: Int = 0
        for x in self {
            if x == Element {
result += 1
}
        }
        return result
    }
}