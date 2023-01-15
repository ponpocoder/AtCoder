#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, m;
  cin >> n >> m;
  vector g(n, vector<int>());
  rep(i, m) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  int res = 0;
  vector<bool> visited(n);
  auto f = [&](auto f, int i) {
    if (visited[i]) return;
    if (res == 1e6) return;
    res++;
    visited[i] = true;
    for(int dest: g[i]) f(f, dest);
    visited[i] = false;
  };
  f(f, 0);
  cout << res << endl;
}
