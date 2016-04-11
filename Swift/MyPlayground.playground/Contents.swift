//: Playground - noun: a place where people can play

import UIKit


func logIfNeeded(log: AnyObject, doWeWantToPrint: Bool=false) {
    if doWeWantToPrint { print("\(log)") }
}
func logIfNeeded(log: Bool, doWeWantToPrint: Bool=false) {
    if doWeWantToPrint { print("\(log)") }
}
print(true)
logIfNeeded("sdf")
logIfNeeded("asdf", doWeWantToPrint: true)
