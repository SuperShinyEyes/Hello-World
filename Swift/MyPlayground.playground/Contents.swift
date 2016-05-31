//: Playground - noun: a place where people can play

import UIKit


func logIfNeeded(log: AnyObject, doWeWantToPrint: Bool=false) {
    if doWeWantToPrint { print("\(log)") }
}

print(true)
logIfNeeded("sdf")
logIfNeeded("asdf", doWeWantToPrint: true)

extension Double {
//    func isNeg()-> Bool = self < 0
    var isNeg: Bool{ return self < 0 }
}

var d: Double = -3
if d.isNeg{
    d = Double.abs(d)
}
print(d)