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

int n, a, b, c;
vector<int> l(n);
const int INF = 1001001;

int dfs(int i, int x, int y, int z) {
  if (i == n) {
    if (x == 0 || y == 0 || z == 0) return INF;
    return abs(a-x)+abs(b-y)+abs(c-z)-30;
  }
  int res = INF;
  res = min(res, dfs(i+1, x, y, z));
  res = min(res, dfs(i+1, x+l[i], y, z)+10);
  res = min(res, dfs(i+1, x, y+l[i], z)+10);
  res = min(res, dfs(i+1, x, y, z+l[i])+10);
  return res;
}

int main() {
  cin >> n >> a >> b >> c;
  l.resize(n);
  rep(i, n) cin >> l[i];
  cout << dfs(0, 0, 0, 0) << endl;
}
