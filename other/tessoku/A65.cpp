#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

vector<int> s;
vector<vector<int>> g;

int dfs(int curr) {
  if (s[curr] != -1) return s[curr];
  int cnt = 0;
  for(int dest: g[curr]) cnt += dfs(dest) + 1;
  return s[curr] = cnt;
}
int main() {
  int n;
  cin >> n;
  g.resize(n+1);
  s.resize(n+1, -1);
  rep(i, n-1) {
    int a;
    cin >> a;
    g[a].push_back(i+2);
  }
  for(int i=1; i<=n; i++) {
    if (i >1) cout << ' ';
    cout << dfs(i);
  }
  cout << endl;
}
