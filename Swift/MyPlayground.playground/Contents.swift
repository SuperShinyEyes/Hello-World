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

let TUAS_2_hall = [[ 24.819228734366149, 60.187057183572854 ], [ 24.819152446040626, 60.186853504694639 ], [ 24.819442836428095, 60.186826619800904 ], [ 24.819519276490329, 60.187030703960268 ], [ 24.819228734366149, 60.187057183572854 ]]

for i in TUAS_2_hall {
    print(i[0])
}
print(TUAS_2_hall[0][0])