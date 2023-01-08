package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	x := make([]string, n)
	for i := range x {
		fmt.Scan(&x[i])
	}
	for i := n - 1; i >= 0; i-- {
		fmt.Println(x[i])
	}
}
