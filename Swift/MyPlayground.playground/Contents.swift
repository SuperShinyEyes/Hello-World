import UIKit

typealias Distance = Double

struct Position {
    var x: Double
    var y: Double
    
    func inRange(range: Distance) -> Bool {
        return sqrt(x*x + y * y) <= range
    }
    
    func minus(p: Position) -> Position {
        return Position(x: x - p.x, y: y - p.y)
    }
    
    var length: Distance {
        return sqrt(x*x + y*y)
    }
}

typealias Region = (Position) -> Bool

struct Ship {
    var position: Position
    var firingRange: Distance
    var unsafeRange: Distance
    
    func canEngageShip(target: Ship) -> Bool {
        let targetDistance = target.position.minus(p: position).length
        return targetDistance <= firingRange
    }
    
    func canSafelyEngageShip(target: Ship, friendly: Ship) -> Bool {
        let targetDistance = target.position.minus(p: position).length
        let friendlyDistance = friendly.position.minus(p: position).length
        return targetDistance <= firingRange &&
            targetDistance > unsafeRange &&
            friendlyDistance > unsafeRange
    }
}

func circle(radius: Distance) -> Region {
    return { point in point.length <= radius }
}

func shift(region: @escaping Region, offset: Position) -> Region {
    return { point in region(point.minus(p: offset)) }
}

let r = shift(region: circle(radius: 10), offset: Position(x: 5, y: 5))
r(Position(x: 2, y: 2))


let a: String? = "Fred"
let b: String? = "Bob"

print(a?.compare(b!))
let height = 100
let offsetY = (true ? -height : height)
print(offsetY)

//func isMultipleOf(n n: Int ) -> Int -> Bool {
//    return{ i in i %n ==0}
//}
//
//func inc( i: inout Int) -> () -> Int {
//    // and capture it in a returned function return 
//    { i += 1; return i }
//}
