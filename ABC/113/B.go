package main

import (
	"fmt"
	"math"
)

func main() {
	var (
		n, res int
		t, a   float64
	)
	var curr float64 = 1001001
	fmt.Scan(&n, &t, &a)
	for i := 0; i < n; i++ {
		var h float64
		fmt.Scan(&h)
		var f float64
		f = math.Abs(a - t + h*0.006)
		if f < curr {
			curr = f
			res = i
		}
	}
	fmt.Println(res + 1)

}
