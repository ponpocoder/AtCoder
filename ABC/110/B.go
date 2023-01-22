package main

import (
	"fmt"
	"math"
)

func main() {
	var n, m int
	var x, y float64
	fmt.Scan(&n, &m, &x, &y)
	ax := make([]int, n)
	ay := make([]int, m)
	var mx = float64(y)
	var mn = float64(x)
	for i := 0; i < n; i++ {
		fmt.Scan(&ax[i])
		mn = math.Max(mn, float64(ax[i]))
	}
	for i := 0; i < m; i++ {
		fmt.Scan(&ay[i])
		mx = math.Min(mx, float64(ay[i]))
	}
	if mn < mx {
		fmt.Println("No War")
	} else {
		fmt.Println("War")
	}
}
