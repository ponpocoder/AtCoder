package main

import "fmt"

func main() {
	var n int
	var s string
	fmt.Scan(&n, &s)
	for i := 1; i < len(s); i++ {
		var l int
		for j := 0; j+i < len(s); j++ {
			if s[j] == s[j+i] {
				break
			}
			l++
		}
		fmt.Println(l)
	}
}
