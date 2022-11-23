#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, x, y;
  cin >> n >> x >> y;
  vector<int> a(n), g(100001);
  rep(i, n) cin >> a[i];
  rep(i, 100001) {
    bool used[3] = {false, false, false};
    if (i >= x) used[g[i-x]] = true;
    if (i >= y) used[g[i-y]] = true;
    if (!used[0]) g[i] = 0;
    else if (!used[1]) g[i] = 1;
    else g[i] = 2;
  }
  int s = 0;
  rep(i, n) s ^= g[a[i]];
  // rep(i, 10) cout << g[i] << endl;
  if (s) cout << "First" << endl;
  else cout << "Second" << endl;
}
