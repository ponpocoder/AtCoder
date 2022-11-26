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
  vector g(n, vector<int>(0));
  rep(i, m) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    g[a].push_back(b);
    g[b].push_back(a);
  }
  vector<int> dist(n, INF);
  queue<int> q;
  q.push(0);
  int cnt = 0;

  while (q.size()) {
    int x = q.size();
    for(int i=0; i< x; i++) {
      int curr = q.front();
      q.pop();
      if (dist[curr] <= cnt) continue;
      dist[curr] = cnt;
      for(int dest: g[curr]) q.push(dest);
    }
    cnt++;
  }
  rep(i, n) {
    if (dist[i] == INF) dist[i] = -1;
    cout << dist[i] << endl;
  }
}
