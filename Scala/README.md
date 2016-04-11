## Ref.
* http://www.scala-lang.org/api/2.11.7/index.html#scala.collection.Seq
* http://alvinalexander.com/scala/scala-programming-cookbook-recipes-faqs
* https://www.cs.helsinki.fi/u/wikla/OTS/Sisalto/examples/html/ch16.html
* https://puzzle.ics.hut.fi/ICS-A1120/2016/notes/round-warmup.html

## Sequence

### Array
```scala
val a = Array(1,2,3,4)
a(0) // 1
a.length
a.reverse
a.take(2)   // Array[Int] = Array(1, 2)
a.drop(2)   // Array[Int] = Array(3, 4)
a.takeRight(2)   // Array[Int] = Array(3, 4)
a.dropRight(2)   // Array[Int] = Array(1, 2)
a.slice(1, 3)    // Array[Int] = Array(2, 3)
iter = a.iterator   // Iterator[Int] = non-empty iterator
iter.next   // 1

/*
.dropWhile :Seq[A]
.endsWith :Boolean
.equals  ==
.exists
.filter
.filterNot
.splitAt
.keys
.filter
.toSet
.toMap
.toVector
.indexWhere
.take
.filterKeys
*/
```

### Sequence operators
```scala
// Prepend
val x = List(1)
val y = 2 +: x   // List[Int] = List(2, 1)

// Append
val x = List(1)
val y = x :+ 2   // List[Int] = List(1, 2)

// Binary operator (= foldLeft)
val a = List(1,2,3,4)
val b = (5 /: a)(_+_)   // b: Int = 15
val c = (50 /: a)((x,y) => x + y)   // c: Int = 60

// Binary operator (= foldRight)
val a = List(1,2,3,4)
val b = (a :\ 10 )(_+_)   // b: Int = 15
val c = (a :\ 50)((x,y) => x + y)   // c: Int = 60

// Convert sequence items to one string
val a = List(1,2,3,4)   // a: List[Int] = List(1, 2, 3, 4)
val b = new StringBuilder()   // b: StringBuilder =
a.addString(b)   // StringBuilder = 1234
a.addString(b, ", ")   // StringBuilder =  "1, 2, 3, 4"
/*
def addString(b: StringBuilder, start: String, sep: String, end: String): StringBuilder
*/
a.addString(b , "List(" , ", " , ")")   // StringBuilder = List(1, 2, 3, 4)

// Item check
a.canEqual(1) ≈ a.contains(1)
/*
canEqual => Equality
*/

// containsSlice
Range(0, 10).containsSlice(Range(1,3))   // true


// CopyToArray
val arr2 = new Array[Int](10)
// arr2: Array[Int] = Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
List(1, 2, 3) copyToArray (arr2, 3)
arr2   // Array[Int] = Array(0, 0, 0, 1, 2, 3, 0, 0, 0, 0)
List(1, 2, 3) copyToArray (arr2)
arr2   // Array[Int] = Array(1, 2, 3, 1, 2, 3, 0, 0, 0, 0)
List(9,9,9) copyToArray (arr2, 0, 2)
arr2   // Array[Int] = Array(9, 9, 3, 1, 2, 3, 0, 0, 0, 0)


// Difference
Range(0, 10) diff Range(5, 15)
// scala.collection.immutable.IndexedSeq[Int] = Vector(0, 1, 2, 3, 4)


// Count occurences
Range(0, 10).count(_ > 5)   // 4

// Remove duplicates
val arr = new Array[Int](10)  // Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
arr.distinct  // Array(0)


// Check property
Range(0, 10).exists(_ > 10)  // False

// Find the first element of the iterable collection
Range(0, 10).find(_ == 1)   // Option[Int] = Some(1)
```



### Range
```scala
Range(0,10)  == 0 until 10
// scala.collection.immutable.Range = Range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```



## Higher Order Functions
```scala
// map
val arr = new Array[Int](10)  // Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
arr.map((x: Int) => x+1) // Array(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

// filter
def isEven(x: Int): Boolean = x % 2 == 0
Range(0, 10).filter(isEven)  // Vector(0, 2, 4, 6, 8)

// reduce
Range(1, 10).reduce((x:Int,y:Int) => x*y)  // 362880
Range(1, 10).reduce(_*_)    // 362880
Range(1, 10).sum            // 45

// fold. Specify initial value for reduce()
Range(1, 10).fold(10)(_+_)    // 55

////////////////////////// scan ////////////////////////////////
a // Array[Int] = Array(752, 884, 995, 462, 126, 632, 445)

a.scanLeft(0)(_ + _) // running sum left-to-right
// Array[Int] = Array(0, 752, 1636, 2631, 3093, 3219, 3851, 4296)

a.scanRight(0)(_ + _) // running sum right-to-left
// Array[Int] = Array(4296, 3544, 2660, 1665, 1203, 1077, 445, 0)

a.scanLeft(100)(_ + _) // start sum from 100
// Array[Int] = Array(100, 852, 1736, 2731, 3193, 3319, 3951, 4396)
////////////////////////////////////////////////////////////////


// zip
Array(1,2,3) zip Array(4,5,6)  // Array((1,4), (2,5), (3,6))

// unzip
Array((1,4), (2,5), (3,6)).unzip // (Array(1, 2, 3),Array(4, 5, 6))

(Array(1,2,3) zip Array(4,5,6)).toMap  // Map(1 -> 4, 2 -> 5, 3 -> 6)
```

### Pairs
```scala
val x = (123,456)   // x: (Int, Int) = (123,456)
x._1                // Int = 123
```

### Cascading
```scala
val a = Array(752, 884, 995, 462, 126, 632, 445)
val result = a.filter(_ % 2 == 0)  // get even elements
              .map(x => x*x)       // square
              .reduce(_ + _)       // sum up
// Returns Int = 1975704

```

## Convert Int to Binary string
```scala
def tellAboutInt(x: Int) {
  print("I am a 32-bit word that Scala views as having format 'Int' ...\n"
     ++ "... my bits are, in binary, ("
        ++ new String((0 to 31)
                        .toArray
                        .map(j => (x >> 31-j)&1)
                        .flatMap(b => "%d".format(b)))
        ++ ")_2\n"
     ++ "... or equivalently, in hexadecimal, 0x%08X\n"
          .format(x)
     ++ "... Scala prints me out as " ++ x.toString ++ "\n"
     ++ "... I represent the signed decimal integer %d\n"
          .format(x)
     ++ "... I represent the unsigned decimal integer %d\n"
          .format(if((x & 0x80000000) != 0) 0x100000000L+x else x)
  )
}
```

## Number system conversion 1
```scala
def toBaseB(a: Int, b: Int): Seq[Int] = {
  require(a >= 0 && b >= 2)
  val r = a%b
  val q = a/b
  if(q > 0) { toBaseB(q,b) :+ r } else { Array(r) }
}
```

## Number system conversion 2
```scala
def fromBaseB(a: Seq[Int], b: Int): Int = {
  require(b >= 2 && a.forall(_ >= 0) && a.forall(_ <= b-1))
  (a :\ (0,1)){ case (aj,(r,bj)) => (r+aj*bj,bj*b) }._1
}
```

## Data Types
### Integers
DataTypes| Size
---|---
Byte|8
Short|16
Int|32
Long|64

### Etc.
DataTypes| Size
---|---
Char|16
String|16 * n
Float|32
Double|64



## Mutable Array
```scala
import scala.collection.mutable.ArrayBuffer

var fruits = ArrayBuffer[String]()
fruits += "Apple"
fruits += "Banana"
fruits += "Orange"
```

## Grouping
```scala
/* partition */
def partition(p: (A) ⇒ Boolean): (List[A], List[A])
val digits = (0 to 9).toList
val evensAndOdds = digits.partition(_ % 2 == 0)
evensAndOdds: (List[Int], List[Int]) = (List(0, 2, 4, 6, 8), List(1, 3, 5, 7, 9))


/* groupBy */
def groupBy[K](f: (A) ⇒ K): Map[K, List[A]]
val evensAndOdds = digits.groupBy {      
    case num: Int if (num % 2 == 0) => "evens"
    case _ => "odds"
}
evensAndOdds: scala.collection.immutable.Map[String,List[Int]] =
    Map(odds -> List(1, 3, 5, 7, 9), evens -> List(0, 2, 4, 6, 8))


/* span */
def span(p: (A) ⇒ Boolean): (List[A], List[A])
digits.span(_ % 2 == 0)
(
  List(0), // the longest prefix of even digits
  List(1, 2, 3, 4, 5, 6, 7, 8, 9) // remaining elements
)


/* grouped */
def grouped(size: Int): Iterator[List[A]]
val groupedByThree = digits.grouped(3)
groupedByThree foreach println
// List(0, 1, 2) List(3, 4, 5) List(6, 7, 8) List(9)


/* splitAt */
def splitAt(position: Int): (List[A], List[A])
digits.splitAt(4)  // ( List(0, 1, 2, 3), List(4, 5, 6, 7, 8, 9) )


/* sliding */
def sliding(size: Int, step: Int): Iterator[List[A]]
val slided = digits.sliding(3, 2)  // Iterator[List[Int]] = non-empty iterator
slided foreach println
// List(0, 1, 2) List(2, 3, 4) List(4, 5, 6) List(6, 7, 8) List(8, 9)
```

## Sorting
```scala
/* Simple sorting */
val digits = List(5, 3, 7, 0, 9, 1, 4, 2, 6, 8)
val ordered = digits.sorted

/* reverse order */
val reverse = digits.sorted(Ordering[Int].reverse)

/* Custom sorting */
scala> case class User(name: String, age: Int)
defined class User

scala> val fred = User("fred", 32)
fred: User = User(fred,32)

scala> val wilma = User("wilma", 29)
wilma: User = User(wilma,29)

scala> val barney = User("barney", 28)
barney: User = User(barney,28)

scala> val betty = User("betty", 21)
betty: User = User(betty,21)

scala> val users = List(betty, fred, barney, wilma)
users: List[User] = List(User(betty,21), User(fred,32), User(barney,28), User(wilma,29))

scala> import scala.math.Orderingimport scala.math.Ordering

scala> val sorted = users.sorted(Ordering.by((_: User).age))sorted: List[User] = List(User(betty,21), User(barney,28), User(wilma,29), User(fred,32))


/* sortBy */
def sortBy[B](f: (A) ⇒ B)(implicit ord: math.Ordering[B]): Seq[A]

val sorted = users.sortBy(_.age)
// List[User] = List(User(betty,21), User(barney,28), User(wilma,29), User(fred,32))
val reverse = users.sortBy(_.age)(Ordering[Int].reverse)
// List[User] = List(User(fred,32), User(wilma,29), User(barney,28), User(betty,21))
val reverse = users.sortBy(u => (u.name, u.age))
// List[User] = List(User(barney,28), User(betty,21), User(fred,32), User(wilma,29))


/* sortWith */
def sortWith(f: (A, A) ⇒ Boolean): Seq[A]

val sorted = users.sortWith(_.age < _.age)
// List[User] = List(User(betty,21), User(barney,28), User(wilma,29), User(fred,32))
val reverse = users.sortWith(_.age > _.age)
// List[User] = List(User(fred,32), User(wilma,29), User(barney,28), User(betty,21))

```

## Scala references
```scala
val a = new InputElement()
val b = new InputElement()
val g1 = new AndGate(a,b)
val g2 = new NotGate(a)
val g3 = new NotGate(b)
val g4 = new AndGate(g2,g3)
val out = new OrGate(g1,g4)
```
![scala-reference](/images/scala-reference.png)

```scala
a.set(false)
```
![eq-diag-stmt1.png](/images/eq-diag-stmt1.png)
```scala
b.set(true)
```
![eq-diag-stmt1.png](/images/eq-diag-stmt2.png)
```scala
/* Fires a sequence of recursive method invocations to compute the value of the Gate-object out. The diagram below summarizes the computation. Each purple arrow is a method call that is made during the computation. Associated with each purple arrow is a green arrow in the reverse direction. This green arrow carries the return value of the method call to the callee. */
out.value
```
![eq-diag-stmt1.png](/images/eq-diag-stmt3.png)

## Scala Code Design
### Initial code
```scala
abstract class Gate() {
  def value: Boolean     // implemented by the extending classes
}

class InputElement() extends Gate() {
  var v = false                         // default value is false
  def set(s: Boolean) { v = s }
  def value = v
}

class NotGate(in: Gate) extends Gate() {
  def value = !in.value
}

class OrGate(in1: Gate, in2: Gate) extends Gate() {
  def value = in1.value || in2.value
}

class AndGate(in1: Gate, in2: Gate) extends Gate() {
  def value = in1.value && in2.value
}

class ConstantGate(v: Boolean) extends Gate() {
  def value = v
}


val a = new InputElement()
val b = new InputElement()
val g1 = new AndGate(a,b)
val g2 = new NotGate(a)
val g3 = new NotGate(b)
val g4 = new AndGate(g2,g3)
val out = new OrGate(g1,g4)
```

### Refined
```scala
abstract class Gate()
{
  def value: Boolean     // implemented by the extending classes
  def not             = new NotGate(this)
  def and(that: Gate) = new AndGate(this, that)
  def or(that: Gate)  = new OrGate(this, that)
}

val a = new InputElement()
val b = new InputElement()
val g1 = a.and(b)
val g2 = a.not
val g3 = b.not
val g4 = g2.and(g3)
val out = g1.or(g4)


// Or even shorter
val a = new InputElement()
val b = new InputElement()
val out = (a.and(b)).or(a.not.and(b.not))
```

### Ultimate concise version
```scala
abstract class Gate() {
  def value: Boolean     // implemented by the extending classes
  def unary_!: Gate        = new NotGate(this)
  def &&(that: Gate): Gate = new AndGate(this, that)
  def ||(that: Gate): Gate = new OrGate(this, that)
}

val a = new InputElement()
val b = new InputElement()
val out = (a && b) || (!a && !b)
```


## Encoding example
### For-loop
```scala
def encode(b: Array[Byte]): String = {
    if (b.length % 3 == 0) restrictedEncode(b)
    else {
      val groupsOfThree = b.grouped(3)
      var encoded = ""
      var concatInt = 0
      for (x <- groupsOfThree) {
        if (x.length == 3) {
          concatInt = to24Bits(x(0), x(1), x(2))
          encoded += to6BitWords(concatInt).map(B64(_)).mkString("")
        } else if (x.length == 2) {
          concatInt = to24Bits(x(0), x(1), 0)
          encoded += to6BitWords(concatInt).map(B64(_)).mkString("")
          encoded = encoded.dropRight(1) + "="
        } else {
          concatInt = to24Bits(x(0), 0, 0)
          encoded += to6BitWords(concatInt).map(B64(_)).mkString("")
          encoded = encoded.dropRight(2) + "=="
        }
      }
    encoded
}
```
### Functional solution
```scala
def encode(b: Array[Byte]): String = {
    val r = b.length%3
    val p = if(r != 0) 3-r else 0

    new String(
        (b ++ Array.fill(p)(0.toByte))
        .grouped(3)
        .toArray
        .map(z => to24Bits(z(0),z(1),z(2)))
        .map(to6BitWords)
        .flatten
        .map(B64(_))
        .dropRight(p)
        ++ Array.fill(p)('='))
}
```

##  Bus Design
```scala
// A custom collection for bus-level building

import collection.SeqLike
import collection.mutable.{ArrayBuffer,Builder}
import collection.generic.CanBuildFrom

class Bus(gates: Seq[Gate])
      extends Seq[Gate]
         with SeqLike[Gate,Bus]
{
  def length = gates.length    // the underlying Seq[Gate]-object implements Seq ops
  def apply(idx: Int) = gates.apply(idx)
  def apply(idxs: Seq[Int]) = new Bus(idxs.map(gates(_)))
  def iterator = gates.iterator

  override protected[this] def newBuilder: Builder[Gate, Bus] = Bus.newBuilder
      // get a builder from companion object

  def values = gates.map(_.value)

  def &&(that: Gate) = new Bus(this.map(_ && that))
  def ||(that: Gate) = new Bus(this.map(_ || that))
  def unary_~        = this.map(!_)
  def &(that: Bus)   = new Bus((this zip that).map(x => x._1 && x._2))
  def |(that: Bus)   = new Bus((this zip that).map(x => x._1 || x._2))
}

object Bus {
  def apply(gates: Gate*) = new Bus(gates)    // Bus(...) companion builder
  def newBuilder: Builder[Gate, Bus] =
    new ArrayBuffer[Gate] mapResult (s => new Bus(s))
      // rely on mutables (ArrayBuffer & Builder) to build Bus objects in the
      // internals of the collections framework
  implicit def canBuildFrom: CanBuildFrom[Bus, Gate, Bus] = {
    new CanBuildFrom[Bus, Gate, Bus] {
      def apply(): Builder[Gate, Bus] = newBuilder
      def apply(from: Bus): Builder[Gate, Bus] = newBuilder
    }
  }
  def inputs(n: Int) = new Bus((1 to n).map(x => Gate.input()))
  def falses(n: Int) = new Bus((1 to n).map(x => Gate.False))
  def trues(n: Int)  = new Bus((1 to n).map(x => Gate.True))
}
```

## Scala Collections
### ArrayBuffer
An ArrayBuffer is an extension of the fixed-size Array provided by the Java Virtual Machine (which in turn relies on the hardware to supply the required memory capacity in consecutively-addressed memory words). Unlike Array, an ArrayBuffer allows the programmer to add new elements to the beginning and end, and also to remove elements:
```scala
import scala.collection.mutable.ArrayBuffer
val a = ArrayBuffer("first", "second")
// a: scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(first, second)
a.append("last")
a.prepend("zeroth")
// a = scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(zeroth, first, second, last)
a.remove(1)
// res: String = first
a
// res: scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(zeroth, second, last)
```
An ArrayBuffer a is in fact an object that internally uses a data structure consisting of
* a fixed-size Array, let us call it array, to store the elements, and
* an integer size0 telling how many of the elements in array are actually in use; that is, the length of the ArrayBuffer a itself.
That is, the internal array can be larger than the current length of a. When a new element is append to the end of a, the algorithm implementing this functionality simply adds the new element in the next free position in array if not all the elements are in use. If the array was already full, then a new internal Array that is twice as long as the old array is allocated and the current contents (and the new element) are copied there. (For the curious: these are implemented in the [ResizableArray trait](http://www.scala-lang.org/api/2.11.7/index.html#scala.collection.mutable.ResizableArray).)

### Map
* immutable.Map
* mutable.Map
* immutable.HashMap
* immutable.ListMap
* mutable.HashMap
* immutable.TreeMap

### [Collection Performances](http://docs.scala-lang.org/overviews/collections/performance-characteristics.html)
**Sequences**
![Scala_collection_performance](/images/Scala_collection_performance_1.png)
**Maps**
![Scala_collection_performance](/images/Scala_collection_performance_2.png)
**Explanation**
![Scala_collection_performance](/images/Scala_collection_performance_3.png)

### Scala supports imperative & functional programming
```scala
// MUTABLE
val m1 = scala.collection.mutable.Map("a"->1, "b"-> 2)
val m2 = m1
m2("c") = 3
m1           // Map(b -> 2, a -> 1, c -> 3)
```
```scala
// IMMMUTABLE
val m1 = scala.collection.immutable.Map("a"->1, "b"-> 2)
val m2 = m1.updated("c", 3)
m1   // Map(a -> 1, b -> 2)
m2   // Map(a -> 1, b -> 2, c -> 3)
```

### Anonymous(Lambda) functions
```scala
val l = Vector(3, 4, 2, 7, 8, 11)
val evens = l.filter(v => v % 2 == 0)
val sumOfEvens = evens.sum
```
```scala
val isEven: Int => Boolean = v => (v % 2 == 0)
isEven(4)    // true
```

### Anonymous(Lambda) functions with pattern matching
```scala
val l = List(1,6,3,7,8,4,5,3)

l.indices // Range(0, 1, 2, 3, 4, 5, 6, 7)

val lWithIndices = l.zipWithIndex
// lWithIndices = List((1,0), (6,1), (3,2), (7,3), (8,4), (4,5), (5,6), (3,7))

val evensWithIndices = lWithIndices.filter({case (num, _) => num % 2 == 0})
// evensWithIndices = List((6,1), (8,4), (4,5))

val result = evensWithIndices.map(_._2)
// result: List[Int] = List(1, 4, 5)
```

```scala
val s = "Turing"

// Imperative style with vars and while loops
var i = 0
while(i < s.length)
  println("s("+i+") = "+s(i))

// With for-loops: this actually is internally implemented roughly as the next one
for(i <- s.indices) {println("s("+i+") = "+s(i)) }

// Functional style alternatives, pick your favorite
s.indices.foreach(i => println("s("+i+") = "+s(i)))

s.zipWithIndex.foreach(p => println("s("+p._2+") = "+p._1))

s.zipWithIndex.foreach({case (char, index) => println("s("+index+") = "+char)})
```

### Multiple cases inside pattern matching
```scala
val l = List("recursion", 2, 2.9)
// l: List[Any] = List(recursion, 2, 2.9)

l.foreach({case s:String => {println("a string of length "+s.length)}
           case n:Int => println("a number")
           case _ => println("an unindentified object") })
// a string of length 9
// a number
// an unindentified object
```

## Treat methods like functions
Scala offers an easy syntax for treating methods defined in objects as functions: we simply add " _ " after the method name to translate it into a function object:
```scala
object areaCalculator {
    def circle(radius: Double) = scala.math.Pi * radius * radius
    def square(side: Double) = side * side
    def rectangle(side1: Double, side2: Double) = side1 * side2
    def triangle(base: Double, height: Double) = base * height * 0.5
}

val circleAreaFunction = areaCalculator.circle _
// circleAreaFunction: Double => Double = <function1>

val circleRadiuses = List(2.0, 3.9, 1.2)
// radiuses: List[Double] = List(2.0, 3.9, 1.2)

val circleAreas = radiuses.map(circleAreaFunction)
// circleAreas: List[Double] = List(12.566370614359172, 47.783624261100755, 4.523893421169302)
```
This ” _ ” -construction is in fact used automatically by the compiler and thus we can simply write:
```scala
val circleAreas = radiuses.map(areaCalculator.circle)
// circleAreas: List[Double] = List(12.566370614359172, 47.783624261100755, 4.523893421169302)
```

### More examples with class methods
```scala
class indentedWriter(s: java.io.PrintStream, prefix: String = "") {
  private var level = 0
  def println(obj: Any) = s.println(prefix + (" "*level) + obj)
  def push {level += 2 }
  def pop {level = 0 max level-2 }
}

val out = new indentedWriter(Console.out, "> ")
val values = Vector(1,2,4)
out.println("The values are:")
out.push
values.foreach(out.println)
out.pop
out.println("Their sum is "+values.sum)

// OUTPUT:
// > The values are:
// >   1
// >   2
// >   4
// > Their sum is 7
```

## forall side effects
```scala
val s = Set(12,2,5,7,11)
s.forall(e => {println(e); e % 4 != 0})
// 5
// 2
// 12
// res: Boolean = false
```

## if-else conditions inside foreach
```scala
val points = Map("40355T"->30, "346823"->70, "826822"->65)
points.foreach(x => println("Student ’"+x._1+"’"+(if(x._2 > 50) "passed" else "did not pass")))
// Student ’40355T’ did not pass
// Student ’346823’ passed
// Student ’826822’ passed
```

## flatMap
```scala
scala> val l = List(1,2,3)
l: List[Int] = List(1, 2, 3)

scala> l.map(v => List(v*2, v*2 + 1))
res: List[List[Int]] = List(List(2, 3), List(4, 5), List(6, 7))

scala> l.flatMap(v => List(v*2, v*2 + 1))
res: List[Int] = List(2, 3, 4, 5, 6, 7)
```

## groupBy
```scala
scala> val names = List("abba", "Turing", "Alabama", "Celsius")
names: List[String] = List(abba, Turing, Alabama, Celsius)

scala> names.groupBy(name => name(0).toLower)
res0: scala.collection.immutable.Map[Char,List[String]] = Map(t -> List(Turing), a -> List(abba, Alabama), c -> List(Celsius))
```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

##
```scala

```

## Get Datatype of an item
```scala
 object.getClass()
```

# Question
```python
def movingSum(l, w):
    return [sum(l[i:i+w]) for i in range(len(l)-w+1)]
```
