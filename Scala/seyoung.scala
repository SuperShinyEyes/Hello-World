val l1 = List(1,2,3,4,5, 0)
val l2 = List(-1,2,0,3,4,-5)

println(l1.filter(i => l2.contains(-i)))
println(l1.reverse)
println(l1.sorted.reverse)
println(l1)
val absolutePairValues = l1.filter(i => l2.contains(-i))
println(absolutePairValues.isEmpty)
// def hasPairSlow(l1: List[Int], l2: List[Int], target: Int): Option[Pair[Int, Int]] = {
//     if (target == 0) {
//         val absolutePairValues = l1.filter(i => l2.contains(-i))
//         if absolutePairValues.isEmpty
//     }
//     ???
// }
