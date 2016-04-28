val combinations = (for {
    i <- 1 to 3 by
    j <- 1 to 3
} yield (i, j))

println(combinations)
