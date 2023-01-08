package main

import "fmt"

func main() {
	var t int
	fmt.Scan(&t)
	for i := 0; i < t; i++ {
		var n, cnt int
		fmt.Scan(&n)
		for j := 0; j < n; j++ {
			var a int
			fmt.Scan(&a)
			if a%2 == 1 {
				cnt++
			}
		}
		fmt.Println(cnt)
	}
}
