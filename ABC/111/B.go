package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	for i := 9; i >= 1; i-- {
		var curr = 100*i + 10*i + i
		if curr-n < 111 {
			fmt.Println(curr)
			return
		}
	}
}
