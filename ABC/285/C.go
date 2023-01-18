package main

import "fmt"

func main() {
	var s string
	fmt.Scan(&s)
	var res int
	for i := 0; i < len(s); i++ {
		res *= 26
		res += int(s[i] - 'A' + 1)
	}
	fmt.Println(res)
}
