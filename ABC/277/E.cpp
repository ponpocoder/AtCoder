#include <iostream>
#include <vector>
#include <deque>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

struct Node {
  int dest, cost;
};

int main() {
  int n, m, k;
  cin >> n >> m >> k;
  int n2 = n*2;
  vector<vector<Node>> g(n2);
  rep(i, m) {
    int u, v, a;
    cin >> u >> v >> a;
    u--; v--;
    if (a == 1) {
      g[u].push_back((Node){v, 1});
      g[v].push_back((Node){u, 1});
    } else {
      g[n+u].push_back((Node){n+v, 1});
      g[n+v].push_back((Node){n+u, 1});
    }
  }
  rep(i, k) {
    int s;
    cin >> s;
    s--;
    g[s].push_back((Node){n+s, 0});
    g[n+s].push_back((Node){s, 0});
  }

  const int INF = 1001001001;
  vector<int> dist(n2, INF);
  dist[0] = 0;
  deque<P> q;
  q.emplace_back(0, 0);
  while (q.size()) {
    auto [curr, cost] = q.front();
    q.pop_front();
    if (dist[curr] != cost) continue;
    for (Node e: g[curr]) {
      int nc = cost + e.cost;
      if (nc >= dist[e.dest]) continue;
      dist[e.dest] = nc;
      if (e.cost) q.emplace_back(e.dest, nc);
      else q.emplace_front(e.dest, nc);
    }
  }

  int res = min(dist[n-1], dist[n2-1]);
  if (res == INF) res = -1;
  cout << res << endl;
}
