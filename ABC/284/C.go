package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	g := make([][]int, n)

	for i := 0; i < m; i++ {
		var u, v int
		fmt.Scan(&u, &v)
		u--
		v--
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}

	visited := make([]bool, n)
	var cnt int
	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}
		cnt++
		dfs(&g, &visited, i)
	}
	fmt.Println(cnt)
}

func dfs(g *[][]int, visited *[]bool, i int) {
	(*visited)[i] = true
	for j := 0; j < len((*g)[i]); j++ {
		if (*visited)[(*g)[i][j]] {
			continue
		}
		dfs(g, visited, (*g)[i][j])
	}
}
