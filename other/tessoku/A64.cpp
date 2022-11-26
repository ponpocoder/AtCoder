#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

const int INF = 1001001001;

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<P>> g(n);
  rep(i, m) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    g[a].push_back(P(b, c));
    g[b].push_back(P(a, c));
  }
  priority_queue<P, vector<P>, greater<P>> q;
  q.push(P(0, 0));
  vector<int> dist(n, INF);
  vector<bool> visited(n);

  while(!q.empty()) {
    P v = q.top();
    q.pop();
    int cd = v.first;
    int curr = v.second;
    if (visited[curr]) continue;
    dist[curr] = cd;
    visited[curr] = true;
    for(auto x : g[curr]) {
      int dest = x.first;
      int cost = x.second;
      if (dist[curr]+cost < dist[dest]) {
        q.push(P(cd+cost, dest));
      }
    }
  }
  rep(i, n) {
    if(dist[i] == INF) dist[i] = -1;
    cout << dist[i] << endl;
  }
}
