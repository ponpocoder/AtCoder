package main

import (
	"fmt"

	"sort"
)

func main() {
	x := make([]int, 3)
	for i := 0; i < 3; i++ {
		fmt.Scan(&x[i])
	}
	sort.Ints(x)
	fmt.Println(x[2]*10 + x[1] + x[0])
}
