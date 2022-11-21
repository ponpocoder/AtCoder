#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  vector<int> v(n), c(n);
  rep(i, n) cin >> v[i];
  rep(i, n) cin >> c[i];
  int res = 0;
  rep(i, n) res += max(0, v[i]-c[i]);
  cout << res << endl;
}
