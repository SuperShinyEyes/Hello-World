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
