//: Playground - noun: a place where people can play

import UIKit

func primes(n: Int) -> [Int] {
    var numbers = [Int](2..<n)
    for i in 0..<n-2 {
        guard let prime = numbers[i] as? Int where prime > 0 else { continue }
        for multiple in (2 * prime - 2).stride(to: n - 2, by: prime) {
            print(prime, multiple, numbers[multiple])
            numbers[multiple] = 0
        }
    }
    return numbers.filter { $0 > 0 }
}

print(primes(20))