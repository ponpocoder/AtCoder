package main

import "fmt"

func main() {
	var n string
	fmt.Scan(&n)
	x := make([]byte, 3)
	for i := 0; i < 3; i++ {
		if n[i] == '1' {
			x[i] = '9'
		} else {
			x[i] = '1'
		}
	}
	fmt.Println(string(x))
}
