package main

import "fmt"

func main() {
    var a, b int
    fmt.Scan(&a, &b)
    if a*2 == b || a*2 + 1 == b {
        fmt.Println("Yes")
    } else {
        fmt.Println("No")
    }
}
