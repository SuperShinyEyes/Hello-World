#!/usr/bin/env python3

## getDigitToProcess(365, 0) => 5
## getDigitToProcess(365, 1) => 6
def getDigitToProcess(n, p):
    return n % pow(10, p+1) // pow(10, p)

def process(array, place):
    rankingArray = [0 for i in range(10)]
    resultArray = [0 for i in range(len(array))]
    for n in array:
        rankingArray[getDigitToProcess(n, place)] += 1

    rankingArray = [sum(rankingArray[:i+1]) for i in range(0, 10)]

    for i in range(len(array)-1, -1, -1):
        number = array[i]
        digit = getDigitToProcess(number, place)
        rankingArray[digit] -= 1
        index = rankingArray[digit]
        resultArray[index] = number

    return resultArray


def radixSort(array):
    resultArray = [0 for i in range(len(array))]
    rankingArray = [0 for i in range(10)]

    iterations = len(str(max(array)))
    for i in range(iterations):
        array = process(array, i)

    print(array)
# process([123,543,2,5546,111], 1)
radixSort([123,543,2,5546,77,94,111])
