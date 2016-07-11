## References
* http://ericasadun.com/2014/06/13/swift-those-ing-swift-variables-unwrapping-and-implicit-unwrapping/
* https://www.andrewcbancroft.com/2015/05/08/strong-weak-and-unowned-sorting-out-arc-and-swift/

## Sequence methods
* `map`
* `contains`
* `dropFirst`
* `dropFirst(num: Int)`
* `dropLast`
* `dropLast(num: Int)`
* `reduce`
* `reverse`
* `flatMap`
* `lexicographicalCompare`
* `elementsEqual`
* `enumerate`
* `flatten`
* `forEach`
* `generate: creates a generator`
* `joinWithSeparator`
  * `["foo", "bar", "baz"].joinWithSeparator("-|-") // "foo-|-bar-|-baz"`
* `maxElement`
* `minElement`
* `prefix` => `take`
* `sort`
* `split`
* `startsWith`
* `suffix` => `takeRight`
* `underestimateCount`
  * Returns a value less than or equal to the number of elements in self, nondestructively.
  * Does not consume a sequence

## String methods
* `startIndex`
* `endIndex`
* `hasPrefix`
* `hasSuffix`
* `capitalizedString`
* `lowercaseString`
* `uppercaseString`
* `componentsSeparatedByString(String)`

## `as?`, `as!`, `is`
* Conversion for `Anyobject`
* Type casting between parent–child classes


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
hello.startIndex
hello.endIndex
hello.hasPrefix("he")
hello.lowercaseString
hello.componentsSeparatedByString("l")
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


## [Heterogenous vs. Homogenous containers](https://medium.com/ios-os-x-development/heterogeneous-vs-homogeneous-generics-630971626b7d#.tse64or9q)
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


## Implement protocol as a class
```swift
protocol SomeProtocol: class {
    func someFunction(SomeView: UIView) -> Double
}

weak var some = SomeProtocol?
```


## Sieve of Eratosthenes
### Stateful
```swift
func primes(n: Int) -> [Int] {
    var numbers = [Int](2..<n)
    for i in 0..<n-2 {
        guard let prime = numbers[i] as? Int where prime > 0 else { continue }
        for multiple in (2 * prime - 2).stride(to: n - 2, by: prime) {
            numbers[multiple] = 0
        }
    }
    return numbers.filter { $0 > 0 }
}
```

### Functional
```swift
func sieve(numbers: [Int]) -> [Int] {
    if numbers.isEmpty { return [] }
    let p = numbers[0]
    return [p] + sieve( numbers[1..<numbers.count].filter { $0 % p > 0 } )
}
```


## Swift value types
* Fundamental types
    * Int, Double, String, ...
* Collections
    * Array, Set, Dictionary
* tuples, structs, enums

## Sort
```swift
var b: [Int] = [3,2,1].sort(<)
```

## Value semantics: Copies are cheap
![copies-are-cheap](/images/copies-are-cheap.png)

### Copy-on-Write
```swift
struct BezierPath: Drawable {
    private var _path = UIBezierPath()

    var pathForReading: UIBezierPath {
        return _path
    }

    var pathForWriting: UIBezierPath {
        mutating get {
            _path = _path.copye() as! UIBezierPath
            return _path
        }
    }
}

extension BezierPath {
    var isEmpty: Bool {
        return pathForReading.isEmpty
    }

    mutating func addLineToPoint(point: CGPoint) {
        pathForWriting.addLineToPoint(point)
    }
}
```

### Copy-on-Write: Uniquely Referenced Swift Objects
```swift
struct MyWrapper {
    var _object: SomeSwiftObject
    var objectForWriting: SomeSwiftObject {
        mutating get {
            if !isUniquelyReferencedNonObjC(&_object) {
                _object = _object.copy()
            }
            return _object
        }
    }
}
```

## Equatable: Make things comparable
```swift
struct Polygon: Equatable {
    var corners: [CGPoint] = []
}

func ==(lhs: Polygon, rhs: Polygon) -> Bool {
    return lhs.corners == rhs.corners
}
```

## mutating: Update value types in struct
```swift
struct Point {
    var x = 0.0, y = 0.0
    mutating func moveByX(deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
}
var somePoint = Point(x: 1.0, y: 1.0)
somePoint.moveByX(2.0, y: 3.0)
print("The point is now at (\(somePoint.x), \(somePoint.y))")
// prints "The point is now at (3.0, 4.0)"
```

## Equality: isEqual vs. ===
```swift
struct Image: Drawable {
    var topLeft: CGPoint
    var image: UIImage
}

extension Image: Equatable { }
func ==(lhs: Image, rhs: Image) -> Bool {
    // Are lhs and rhs refer to the same object/image?
    return lhs.topLeft == rhs.topLeft && lhs.image === rhs.image

    // Do lhs and rhs have the same bitmap image?
    return lhs.topLeft == rhs.topLeft && lhs.image.isEqual(rhs.image)
}
```

## Optionals can be chained
```swift
var UILabel?
if let label = display {
    if let text = label.text {
        let x = text.hashValue
    }
}

// or

if let x: Optional<Int> = display?.text?.hashValue { ... }
```

## ??
```swift
let s: String? = ...
if s != nil {
    display.text = s
} else {
    display.text = " "
}

// or
display.text = s ?? " "
```

## Tuples
```swift
let x: (String, Int, Double) = ("hello", 5, 5.4)
let (word, number, value) = x

// or
let x: (w: String, i: Int, v: Double) = ("hello", 5, 5.4)
print(x.w)
```

## Classes vs. structs vs. enums
![Classes vs. structs vs. enums](/images/Classes vs. structs vs. enums.png)

## Swift Methods
![SwiftMethods](/images/SwiftMethods.png)
![SwiftMethods](/images/SwiftMethods2.png)

## If let optional
```swift
@IBAction func touchDigit(sender: UIButton) {
        if let digit = sender.currentTitle as String! {
            print("\(digit)")
        } else {
            print("No data")
        }
    }
```

## Struct doesn't need init()
```swift
struct Character {
   enum CharacterType {
    case Thief
    case Warrior
    case Knight
  }
  enum Weapon {
    case Bow
    case Sword
    case Lance
    case Dagger
  }
  let type: CharacterType
  let weapon: Weapon
}

let warrior = Character(type: .Warrior, weapon: .Sword)
```

## [Pattern matching](https://appventure.me/2015/08/20/swift-pattern-matching-in-detail/)
```swift
enum TraderType {
case SingleGuy
case Company
}

enum Trades {
    case Buy(stock: String, amount: Int, stockPrice: Float, type: TraderType)
    case Sell(stock: String, amount: Int, stockPrice: Float, type: TraderType)
}

let aTrade = Trades.Sell(stock: "GOOG", amount: 100, stockPrice: 666.0, type: TraderType.Company)

switch aTrade {
case let .Buy(stock, amount, _, TraderType.SingleGuy):
    processSlow(stock, amount, 5.0)
case let .Sell(stock, amount, _, TraderType.SingleGuy):
    processSlow(stock, -1 * amount, 5.0)
case let .Buy(stock, amount, _, TraderType.Company):
    processFast(stock, amount, 2.0)
case let .Sell(stock, amount, _, TraderType.Company):
    processFast(stock, -1 * amount, 2.0)
}
```

### Wild card pattern
```swift
let p: String? = nil
switch p {
case _?: print ("Has String")
case nil: print ("No String")
}
```

### Tuple Pattern
```swift
let age = 23
let job: String? = "Operator"
let payload: AnyObject = NSDictionary()

switch (age, job, payload) {
  case (let age, _?, _ as NSDictionary):
  print(age)
  default: ()
}
```

### Expression pattern
```swift
switch 5 {
  case 0...10: print("In range 0-10")
  default: break
}
```

```swift
struct Soldier {
    let hp: Int
    let x: Int
    let y: Int
}

extension Soldier {
    func unapply() -> (Int, Int, Int) {
        return (self.hp, self.x, self.y)
    }
}

func ~= (p: (Int, Int, Int), t: (Int, Int, Int)) -> Bool {
    return p.0 == t.0 && p.1 == t.1 && p.2 == t.2
}

let soldier = Soldier(hp: 99, x: 10, y: 10)
print(soldier.unapply() ~= (99, 10, 10))
```

## init(_ val: Int)
```swift
struct Celsius {
    var temperature: Double

    init(fromFahrenheit fahrenheit: Double) {
        temperature = (fahrenheit - 32) / 1.8
    }

    init(fromKelvin kelvin: Double) {
        temperature = kelvin - 273.15
    }

    init(_ celsius: Double) {
        temperature = celsius
    }
}

let boilingPointOfWater = Celsius(100)
let freezingPointOfWater = Celsius(fromKelvin: 273.15)
```

## Fallthrough
```swift
switch 5 {
   case 5:
    print("Is 5")
    fallthrough
   default:
    print("Is a number")
}
// Will print: "Is 5" "Is a number"
```

## Loop in pattern matching
```swift
gameLoop: while true {
  switch state() {
     case .Waiting: continue gameLoop
     case .Done: calculateNextState()
     case .GameOver: break gameLoop
  }
}
```

## Optional pattern matching
```swift
var result: String? = secretMethod()
switch result {
case nil:
    print("is nothing")
case let a?:
    print("\(a) is a value")
}
```

## filter, map, flatMap
```swift
let wordFreqs = [("k", 5), ("a", 7), ("b", 3)]
let res2 = wordFreqs.filter({ e in e.1 > 3 }).map {$0.0}
// ["k", "a"]
let res3 = wordFreqs.filter({ $0.1 > 3 }).map {$0.0}

let res4 = wordFreqs.flatMap { (e) -> String? in
    switch e {
    case let (s, t) where t > 3: return s
    default: return nil
    }
}

let res5 = wordFreqs.flatMap { (e) -> String? in if e.1 > 3 {return e.0} else {return nil}
}
```

## [`guard let case` vs. `if let case`](http://alisoftware.github.io/swift/pattern-matching/2016/05/16/pattern-matching-4/)

* `guard` ensures you not to "fallthrough"
* `guard` must **return** or **continue** when the pattern doesn't match =>
  * `guard` mostly used inside functions
  * inside a `for-loop` with `continue`
* `if let case` can be used anywhere and doesn't need to return anything.
* `if case let x = y { … }` === `switch y { case let x: … }`


```swift
enum Media {
  case Book(title: String, author: String, year: Int)
  case Movie(title: String, director: String, year: Int)
  case WebSite(urlString: String)
}
let m = Media.Movie(title: "Captain America: Civil War", director: "Russo Brothers", year: 2016)

// if case let
if case let Media.Movie(title, _, _) = m {
  print("This is a movie named \(title)")
}

// switch
switch m {
  case let Media.Movie(title, _, _):
    print("This is a movie named \(title)")
  default: () // do nothing, but this is mandatory as all switch in Swift must be exhaustive
}

// if case let where
if case let Media.Movie(_, _, year) = m where year < 1888 {
    print("Something seems wrong: the movie's year is before the first movie ever made.")
  }
```
```swift
// guard case let
enum NetworkResponse {
  case Response(NSURLResponse, NSData)
  case Error(NSError)
}

func processRequestResponse(response: NetworkResponse) {
  guard case let .Response(urlResp, data) = response,
    let httpResp = urlResp as? NSHTTPURLResponse
    where 200..<300 ~= httpResp.statusCode else {
      print("Invalid response, can't process")
      return
  }
  print("Processing \(data.length) bytes…")
  /* … */
}
```
`for case` is like `if case` inside a for-loop
```swift
let mediaList: [Media] = [
  .Book(title: "Harry Potter and the Philosopher's Stone", author: "J.K. Rowling", year: 1997),
  .Movie(title: "Harry Potter and the Philosopher's Stone", director: "Chris Columbus", year: 2001),
  .Book(title: "Harry Potter and the Chamber of Secrets", author: "J.K. Rowling", year: 1999),
  .Movie(title: "Harry Potter and the Chamber of Secrets", director: "Chris Columbus", year: 2002),
  .Book(title: "Harry Potter and the Prisoner of Azkaban", author: "J.K. Rowling", year: 1999),
  .Movie(title: "Harry Potter and the Prisoner of Azkaban", director: "Alfonso Cuarón", year: 2004),
  .Movie(title: "J.K. Rowling: A Year in the Life", director: "James Runcie", year: 2007),
  .WebSite(urlString: "https://en.wikipedia.org/wiki/List_of_Harry_Potter-related_topics")
]

for case let Media.Movie(title, director, year) in mediaList where director == "Chris Columbus" {
  print(" - \(title) (\(year))")
}
// - Harry Potter and the Philosopher's Stone (2001)
// - Harry Potter and the Chamber of Secrets (2002)

for media in mediaList {
    guard let title = media.title else { continue }
    guard title.hasPrefix("Harry Potter") else { continue }
    print(" - [\(media.kind)] \(title)")
}
```

## Fonts
```swift
static func preferredFontForTextStyle(UIFontTextStyle) -> UIFont
// UIFontTextStyle.Body, UIFontTextStyle.Footernote, etc.
```
## Protocls
### `weak` in closure
![weak_in_closures](/images/weak_in_closures.png)
```swift
protocol Moveable {
    mutating func moveTo(p: CGPoint)
}
class Car: Moveable {
    func moveTo(p: CGPoint) {...}
    func changeOil()
}
struct Shape: Moveable {
    mutating func moveTo(p: CGPoint) { ... }
    func draw()
}

let prius: Car = Car()
let square: Shape = Shape()

var thingToMove: Moveable = prius
thingToMove.moveTo(...)     // Works
thingToMove.changeOil(...)  // Fails
thingToMove = square
let thingsToMove: [Moveable] = [prius, square]

func slide(slider: Moveable) {
    let positionToSlideTo = ..
    slider.moveTo(positionToSlideTo)
}
slide(prius); slide(square)
// x must inherit Slippery and Moveable
func slipAndSlide(x: protocol<Slippery, Moveable>)
slipAndSlide(prius)  // Fails
```

## Get time interval/difference
```swift
NSDate().timeIntervalSinceNow
```

## Fetch data from the Internet
```swift
private func fetchImage() {
    if let url = imageURL {
        if let imageData = NSData(contentsOfURL: url) {
            image = UIImage(data: imageData)
        }
    }
}
```

## Multithreading
### Executing a function on another queue
```swift
let queue: dispatch_queue_t = // get the queue you want
dispatch_async(queue) { /* Do what you want to do in the closure */ }
```
### Main queue(a *serial* queue)
```swift
let mainQ: dispatch_queue_t = dispatch_get_main_queue()
// All UI stuff must be done on this queue
// And all time-consuming stuff must be done off this queue
dispatch_async(not the main queue){
    // do a non-UI that might block or otherwise takes a while
    dispatch_async(dispatch_get_main_queue()){
        // call UI functions with the results of the above
    }
}
```
### Non-main-queues
```swift
// QOS = Quality of Service
QOS_CLASS_USER_INTERACTIVE  // quick and high priority
QOS_CLASS_USER_INITIATED    // high priority, might take time
QOS_CLASS_UTILITY           // long running
QOS_CLASS_BACKGROUND        // user not concerned with this (prefetching, etc)
let queue = dispatch_get_global_queue(QOS_CLASS_USER_INITIATED, 0)  
// 0 is a "reserved for future"
```
### You can create your own serial queue
```swift
let serialQ = dispatch_queue_create("name", DISPATCH_QUEUE_SERIAL)
```
### Example
```swift
let session = NSURLSession(configuration: NSURLSessionConfiguration.defaultSessionConfiguration())
if let url = NSURL(string: "http://url") {
    let request = NSURLRequest(URL:url)
    let task session.downloadTaskWithRequest(request) { (localURL, response, error) in
        /* Do UI stuff AFTER you dispatch back to main queue while downloading  */
        dispatch_async(dispatch_get_main_queue()) {
            /* Do UI stuff here*/
        }
    }
    task.resume()
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

##
```swift
```

##
```swift
```
