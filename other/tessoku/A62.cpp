#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

void dfs(int curr, unordered_set<int> &s, vector<vector<int>> &g) {
  if (s.count(curr)) return;
  s.insert(curr);
  for(int dest: g[curr]) {
    dfs(dest, s, g);
  }
}

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
  unordered_set<int> s;
  dfs(0, s, g);
  if ((int)s.size() == n) cout << "The graph is connected." << endl;
  else cout << "The graph is not connected." << endl;
}
