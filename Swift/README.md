## References
* http://ericasadun.com/2014/06/13/swift-those-ing-swift-variables-unwrapping-and-implicit-unwrapping/
* https://www.andrewcbancroft.com/2015/05/08/strong-weak-and-unowned-sorting-out-arc-and-swift/

## guard
```swift
func session(session: WCSession, didReceiveMessage message: [String: AnyObject]) {
    guard message["request"] as? String == "fireLocalNotification" else{
        return
    }

    let localNotification = buildLocalNotifcation()
    UIApplication.sharedApplication().scheduleLocalNotification(localNotification)
}
```
![watchOS-structure](/images/watchOS-structure.png)

## [Automatic Reference Counting](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html)
### Example of circular reference
```swift
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
```
![referenceCycle02_2x.png](/images/referenceCycle02_2x.png)
### Solve with weak
```swift
class Person {
    let name: String
    init(name: String) { self.name = name }
    var apartment: Apartment?
    deinit { print("\(name) is being deinitialized") }
}

class Apartment {
    let unit: String
    init(unit: String) { self.unit = unit }
    weak var tenant: Person?
    deinit { print("Apartment \(unit) is being deinitialized") }
}

var john: Person?
var unit4A: Apartment?

john = Person(name: "John Appleseed")
unit4A = Apartment(unit: "4A")

john!.apartment = unit4A
unit4A!.tenant = john
```
![weakReference01_2x.png](/images/weakReference01_2x.png)

### Unowned reference
```swift
class Customer {
    let name: String
    var card: CreditCard?
    init(name: String) {
        self.name = name
    }
    deinit { print("\(name) is being deinitialized") }
}

class CreditCard {
    let number: UInt64
    unowned let customer: Customer
    init(number: UInt64, customer: Customer) {
        self.number = number
        self.customer = customer
    }
    deinit { print("Card #\(number) is being deinitialized") }
}

var john: Customer?
john = Customer(name: "John Appleseed")
john!.card = CreditCard(number: 1234_5678_9012_3456, customer: john!)
```
![unownedReference01_2x.png](/images/unownedReference01_2x.png)


### Unowned References and Implicitly Unwrapped Optional Properties
```swift
class Country {
    let name: String
    var capitalCity: City!
    init(name: String, capitalName: String) {
        self.name = name
        self.capitalCity = City(name: capitalName, country: self)
    }
}

class City {
    let name: String
    unowned let country: Country
    init(name: String, country: Country) {
        self.name = name
        self.country = country
    }
}

var country = Country(name: "Canada", capitalName: "Ottawa")
```

### Resolving Strong Reference Cycles for Closures
Example case
```swift
class HTMLElement {

    let name: String
    let text: String?

    lazy var asHTML: Void -> String = {
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }

    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }

    deinit {
        print("\(name) is being deinitialized")
    }

}

let heading = HTMLElement(name: "h1")
let defaultText = "some default text"
heading.asHTML = {
    return "<\(heading.name)>\(heading.text ?? defaultText)</\(heading.name)>"
}
print(heading.asHTML())
// prints "<h1>some default text</h1>"

var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
print(paragraph!.asHTML())
// prints "<p>hello, world</p>"
```
![closureReferenceCycle01_2x.png](/images/closureReferenceCycle01_2x.png)

Solution
```swift
class HTMLElement {

    let name: String
    let text: String?

    lazy var asHTML: Void -> String = {
        [unowned self] in
        if let text = self.text {
            return "<\(self.name)>\(text)</\(self.name)>"
        } else {
            return "<\(self.name) />"
        }
    }

    init(name: String, text: String? = nil) {
        self.name = name
        self.text = text
    }

    deinit {
        print("\(name) is being deinitialized")
    }

}

var paragraph: HTMLElement? = HTMLElement(name: "p", text: "hello, world")
print(paragraph!.asHTML())
// prints "<p>hello, world</p>"

paragraph = nil
// prints "p is being deinitialized"
```
![closureReferenceCycle02_2x.png](/images/closureReferenceCycle02_2x.png)

Define a capture List
```swift
lazy var someClosure: (Int, String) -> String = {
    [unowned self, weak delegate = self.delegate!] (index: Int, stringToProcess: String) -> String in
    // closure body goes here
}
```
Implicit way
```scala
lazy var someClosure: Void -> String = {
    [unowned self, weak delegate = self.delegate!] in
    // closure body goes here
}
```

## Extension
```swift
extension Int {
    func repeat(block : () -> ()) {
        for i in 0..<self {
            block()
        }
    }
}

3.repeat {
    println("hello")   // called 3 times
}
```


## [Enumeration cases](http://www.drewag.me/posts/7-cool-features-in-swift#enumeration-cases-can-hold-values)
```swift
struct NetRequest {
    enum Method {
        case GET
        case POST(String)
    }

    var URL: String
    var method: Method
}

var getRequest = NetRequest(URL: "http://drewag.me", method: .GET)
var postRequest = NetRequest(URL: "http://drewag.me", method: .POST("{\"username\": \"drewag\"}"))
```

```swift
class Word {
    enum PartOfSpeech {
        case Noun, Pronoun, Verb
    }

    var value: String
    var partOfSpeech: PartOfSpeech

    init(_ value: String, _ partOfSpeech: PartOfSpeech) {
        self.value = value
        self.partOfSpeech = partOfSpeech
    }
}
var sentence = [Word("I", .Pronoun), Word("ran", .Verb), Word("home", .Noun)]
sentence.append("quickly") // Cannot convert the expression's type '()' to type 'Word'
sentence[0].lowercaseString // Could not find member 'lowercaseString'
sentence[0].value.lowercaseString
```


## Optional
The Swift compiler helps us with some syntactic sugar, but in reality when you define an optional String like this: var myString : String? the compiler actually translates it to var myString : Optional<String>. An Optional is defined as follows:
```swift
enum Optional {
    case None
    case Some(T)
}
```


## [Lazily Calculated Member Variables](http://stackoverflow.com/questions/24006975/why-create-implicitly-unwrapped-optionals)
Sometimes you have a member variable that should never be nil, but it cannot be set to the correct value during initialization. One solution is to use an Implicitly Unwrapped Optional, but a better way is to use a lazy variable:
```swift
class FileSystemItem {
}

class Directory : FileSystemItem {
    lazy var contents : [FileSystemItem] = {
        var loadedContents = [FileSystemItem]()
        // load contents and append to loadedContents
        return loadedContents
    }()
}
```


## Where clause with optional
```swift
if let firstNumber = Int("4"), secondNumber = Int("42") where firstNumber < secondNumber {
    print("\(firstNumber) < \(secondNumber)")
}
// prints "4 < 42"
```


## Initialize an empty array
```swift
var operandStack: Array<Double> = Array<Double>()
```

## Properties
### Read-only properties
```swift
struct Cuboid {
    var width = 0.0, height = 0.0, depth = 0.0
    var volume: Double {
        return width * height * depth
    }
}
```

### Getter & Setter
If a computed property’s setter does not define a name for the new value to be set, a default name of newValue is used.
```swift
struct AlternativeRect {
    var origin = Point()
    var size = Size()
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set {
        // Or you could have given a parameter name
        // set(newCenter) {

            origin.x = newValue.x - (size.width / 2)
            origin.y = newValue.y - (size.height / 2)
        }
    }
}
```

### willSet & didSet
```swift
class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newTotalSteps) {
            print("About to set totalSteps to \(newTotalSteps)")
        }
        didSet {
            if totalSteps > oldValue  {
                print("Added \(totalSteps - oldValue) steps")
            }
        }
    }
}
let stepCounter = StepCounter()
stepCounter.totalSteps = 200
// About to set totalSteps to 200
// Added 200 steps
stepCounter.totalSteps = 360
// About to set totalSteps to 360
// Added 160 steps
stepCounter.totalSteps = 896
// About to set totalSteps to 896
// Added 536 steps
```

## Clojure

### Pass function as a parameter
```swift
func performOperation(operation: (Double, Double) -> Double) {
    operation(operandStack.removeLat(), operandStack.removeLat())
}

case "×": performOperation(multiply)
case "−": performOperation(subtract)
case "+": performOperation(add)
case "÷": performOperation(divide)

func multiply(n1: Double, n2:Double) -> Double { return n1 * n2 }
func add(n1: Double, n2:Double) -> Double { return n1 + n2 }
func subtract(n1: Double, n2:Double) -> Double { return n1 - n2 }
func divide(n1: Double, n2:Double) -> Double { return n1 / n2 }
```

### Basic clojure
```swift
case "×": performOperation({ (op1: Double, op2: Double) -> Double in return op1 * op2 })
case "−": performOperation({ (op1: Double, op2: Double) -> Double in return op1 - op2 })
case "+": performOperation({ (op1: Double, op2: Double) -> Double in return op1 + op2 })
case "÷": performOperation({ (op1: Double, op2: Double) -> Double in return op1 / op2 })
```

### Without return when it's specified
```swift
case "×": performOperation({ (op1, op2) in return op1 * op2 })
case "−": performOperation({ (op1, op2) in return op1 - op2 })
case "+": performOperation({ (op1, op2) in return op1 + op2 })
case "÷": performOperation({ (op1, op2) in return op1 / op2 })
```

### Without return when it's specified
```swift
case "×": performOperation({ (op1, op2) in op1 * op2 })
case "−": performOperation({ (op1, op2) in op1 - op2 })
case "+": performOperation({ (op1, op2) in op1 + op2 })
case "÷": performOperation({ (op1, op2) in op1 / op2 })
```

### Almost The Most Concise
```swift
case "×": performOperation({ $0 * $1 })
case "−": performOperation({ $0 - $1 })
case "+": performOperation({ $0 + $1 })
case "÷": performOperation({ $0 / $1 })
```

### The Most Concise
```swift
case "×":performOperation { $0 * $1 }
case "−":performOperation { $0 - $1 }
case "+":performOperation { $0 + $1 }
case "÷":performOperation { $0 / $1 }
```

##
```swift

```

##
```swift

```

##
```swift

```

##
```swift

```

##
```swift

```

##
```swift

```

##
```swift

```
