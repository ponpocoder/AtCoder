#include <iostream>
#include <map>
#include <vector>
#include <queue>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n = 9;
  int m;
  cin >> m;
  vector<vector<int>> graph(n);
  rep(i, m) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    graph[u].push_back(v);
    graph[v].push_back(u);
  }

  vector<int> p(n, -1);
  rep(i, n-1) {
    int x;
    cin >> x;
    x--;
    p[x] = i;
  }
  vector<int> t(n, -1);
  rep(i, n-1) t[i] = i;
  map<vector<int>, int> dist;
  dist[p] = 0;
  queue<vector<int>> q;
  q.push(p);
  while (q.size()) {
    vector<int> curr = q.front();
    q.pop();
    int d = dist[curr];
    rep(i, n) if (curr[i] == -1) {
      for (int dest: graph[i]) {
        vector<int> nx = curr;
        swap(nx[i], nx[dest]);
        if (dist.find(nx) == dist.end()) {
          dist[nx] = d+1;
          q.push(nx);
        }
      }
    }
  }
  if (dist.find(t) == dist.end()) cout << -1 << endl;
  else cout << dist[t] << endl;
}
