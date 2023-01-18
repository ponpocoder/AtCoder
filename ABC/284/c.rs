use proconio::{input, marker::Usize1};

fn main() {
    input! {
        n: usize,
        m: usize,
        uv: [(Usize1, Usize1); m],
    }
    let mut g = vec![Vec::new(); n];
    for (u, v) in uv {
        g[u].push(v);
        g[v].push(u);
    }

    let mut cnt  = 0;
    let mut visited = vec![false; n];

    for i in 0..n {
        if dfs(i, &g, &mut visited) {
            cnt += 1;
        }
    }
    println!("{}", cnt);
}

fn dfs(i: usize, g: &[Vec<usize>], visited: &mut [bool]) -> bool {
    if visited[i] {
        return false;
    }
    visited[i] = true;
    for j in &g[i] {
        dfs(*j, g, visited);
    }
    true
}
