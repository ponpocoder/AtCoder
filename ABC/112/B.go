package main

import "fmt"

func main() {
	var n, T int
	const INF int = 1001001
	res := INF
	fmt.Scan(&n, &T)
	for i := 0; i < n; i++ {
		var c, t int
		fmt.Scan(&c, &t)
		if t <= T {
			if c < res {
				res = c
			}
		}
	}
	if res == INF {
		fmt.Println("TLE")
	} else {
		fmt.Println(res)
	}
}
