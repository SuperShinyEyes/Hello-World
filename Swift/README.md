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


## Optional is just an enum
The Swift compiler helps us with some syntactic sugar, but in reality when you define an optional String like this: var myString : String? the compiler actually translates it to var myString : Optional<String>. An Optional is defined as follows:
```swift
enum Optional {
    case None
    case Some(T)
}

let x: String? = nil  // is equal to
let x = Optional<String>.None

let x: String? = "hello"  // is equal to
let x = Optional<String>.Some("hello")

var y = x!    // is ...
switch x {
    case Some(let value): y = value
    case None:  // raise an exception
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

### The Most Concise with only functions
```swift
case "×":performOperation(*)
case "−":performOperation(-)
case "+":performOperation(+)
case "÷":performOperation(/)
```

## Enum
### Make Enum printable using the protocol, CustomStringConvertible
```swift
private enum Op: CustomStringConvertible {
    case Operand(Double)
    case UnaryOperation(String, Double -> Double)
    case BinaryOperation(String, (Double, Double) -> Double)

    var description: String {
        get {
            switch self {
            case .Operand(let operand):
                return "\(operand)"
            case .UnaryOperation(let symbol, _):
                return symbol
            case .BinaryOperation(let symbol, _):
                return symbol
            }
        }
    }
}

private var knownOps = Dictionary<String, Op>()
```

### Generate enum instances
```swift
init() {
    knownOps["×"] = Op.BinaryOperation("×", *)
    knownOps["−"] = Op.BinaryOperation("−", -)
    knownOps["+"] = Op.BinaryOperation("+", +)
    knownOps["÷"] = Op.BinaryOperation("÷", /)
    knownOps["√"] = Op.UnaryOperation("√", sqrt)
}
```

### Generate enum instances more elegantly
```swift
init() {
    func learnOp(op: Op) {
        knownOps[op.description] = op
    }
    learnOp(Op.BinaryOperation("×", *))
    learnOp(Op.BinaryOperation("−", -))
    learnOp(Op.BinaryOperation("+", +))
    learnOp(Op.BinaryOperation("÷", /))
    learnOp(Op.UnaryOperation("√", sqrt))
}
```

## Struct
```swift
struct MyStruct {
    var x: Int 42
    var y: String "haha"

    init(x: Int, y: String)  // default
}
```


## Range
```swift
let array = [1,2,3,4,5]
let arraySimple = array[1...5]
let arraySimple2 = array[1..<6]
for i in [1...10] {}
```

## Swift & Objective-C lasses
* NSObject
    * Base class for all Objective-C classes. Some advanced features will require you to subclass from NSObject
* NSNumber
    * let n = NSNumber(35.3)
    * n.intValue
* NSDate
    * localization ramification
    * NSCalendar, NSDateFormatter, NSDateComponents
* NSData
    * A "bag o' bits"

## Lazy Initialization
### Only 'var' can be *lazy*!
```swift
lazy var someProperty: Type = {
    // Construct the value of someProperty
    return <the constructed value>
}

lazy var myProperty = self.initializeMyProperty()
```

## Failable init
```swift
init?(arg1: Type1, ...) {
    // might return nil
}

if let image = UIImage(named: "foo") {
    // image was successfully created
} else {
    // couldn't create the image
}

```

## AnyObject – it's a protocol
```swift
var destinationViewController: AnyObject

// Generally,
if let calcVC = destinationViewController as? CalculatorViewController {
    // iff destinationViewController was a type of CalculatorViewController
}

// Check before we even try to do as with the is keyword,
if destinationViewController is CalculatorViewC ontroller { }
```
### Caseting Arrays of AnyObject
```swift
var toolbarItems: [AnyObject]
for item in toolbarItems {
    if let toolbarItem = item as? UIBarButtonItem { }
}

// If you know the types for sure
for toolbarItem in toolbarItems as [UIBarButtonItem] {
    // crashes if it's nil. Can't use 'as?'
}
```

### More examples on AnyObject
```swift
// Create a button in code
let button: AnyObject = UIButton.buttonWithType(UIButtonType.System)

let title = (button as UIButton).currentTitle  // Crashes if not UIButton
```

## Methods
### Array<T>
```swift
var a = [1,2,3]
a += [4,5,6]
// append(T)
// insert(T, atIndex: Int)
// splice(Array<T>, atIndex: Int)
// removeAtIndex(Int)
// removeRange(Range)
// replaceRange(Range, [T])
// a.sort
// a.sort {$0 > $1}
// a.filter {_ % 2 == 0}
let stringified: [String] = a.map { "\($0)" }
let reduced: Int = a.reduce(0) {$0 + $1}
```

### String
```swift
var hello = "hello"
let index = hello.startIndex.advancedBy(3)
print(hello[index])  // "l\n"
hello.substringFromIndex(index)
hello.substringWithRange(Range<String.Index>(start: hello.startIndex.advancedBy(0), end: hello.endIndex.advancedBy(-3)))
hello.appendContentsOf("koko")
hello.capitalizedString
hello.insertContentsOf("koko".characters, at: hello.startIndex.advancedBy(3))
```


## Type Conversion
Convert by creating a new object
```swift
let d: Double = 37.5
let f: Float = 37.5
let x = Int(d)
let xd = Double(x)
let cgf = CGFloat(d)
String(42)
```


## Drawing
```swift
@IBDesignable
class ....      // View the drawing on storyboard on-the-fly

@IBInspectable
var ....        // Access the field on right side inspection tool
```


## Constraining value range
```swift
var age: Int = 0 {
    didSet {
        age = min(max(age, 0), 100)
    }
}
```

## Identity Operators for reference types, i.e., class instances
```swift
===     // Identical to
!==     // Not identical to
```

## Struct vs. Class
* Struct
    * The structure’s primary purpose is to encapsulate a few relatively simple data values.
    * It is reasonable to expect that the encapsulated values will be copied rather than referenced when you assign or pass around an instance of that structure.
    * Any properties stored by the structure are themselves value types, which would also be expected to be copied rather than referenced.
    * The structure does not need to inherit properties or behavior from another existing type.
*

## [Type properties](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Properties.html)
```swift
struct AudioChannel {
    static let thresholdLevel = 10
    static var maxInputLevelForAllChannels = 0
    var currentLevel: Int = 0 {
        didSet {
            if currentLevel > AudioChannel.thresholdLevel {
                // cap the new audio level to the threshold level
                currentLevel = AudioChannel.thresholdLevel
            }
            if currentLevel > AudioChannel.maxInputLevelForAllChannels {
                // store this as the new overall maximum input level
                AudioChannel.maxInputLevelForAllChannels = currentLevel
            }
        }
    }
}

var jbl = AudioChannel()
jbl.currentLevel = 5
print(AudioChannel.maxInputLevelForAllChannels)  // 5
```

```swift
struct SomeStructure {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 1
    }
}
enum SomeEnumeration {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 6
    }
}
class SomeClass {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    // Below can be overrided by subclasses
    class var overrideableComputedTypeProperty: Int {
        return 107
    }
}
```


## Heterogenous vs. Homogenous containers
![heterogenous_vs_homogenous](/images/heterogenous_vs_homogenous.png)

```swift
protocol Ordered {
  func precedes(other: Self) -> Bool
}

struct Number : Ordered {
  var value: Double = 0
  func precedes(other: Number) -> Bool {
    return self.value < other.value
  }
}

func binarySearch<T : Ordered>(sortedKeys: [T], forKey k: T) -> Int {
  var lo = 0
  var hi = sortedKeys.count
  while hi > lo {
    let mid = lo + (hi - lo) / 2
    if sortedKeys[mid].precedes(k) { lo = mid + 1 }
    else { hi = mid }
    }
  return lo
}
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


##
```swift

```


##
```swift

```
