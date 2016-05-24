println((20 to 10 by -1).zipWithIndex.sorted)
println(Array("a", "b", "c") zip (Stream from 1))

val a = Array(("Seyoung", 100), ("Seyoung", 300), ("Heeryung", 100))
val b = a.groupBy(_._1)
b.reduce((a,b) => (a._1, a._2+b._2))
