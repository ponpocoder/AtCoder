#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, c;
  cin >> n >> c;
  vector<int> x(2);
  x[1] = ~0;
  rep(i, n) {
    int t, a;
    cin >> t >> a;
    rep(j, 2) {
      if (t == 1) x[j] &= a;
      if (t == 2) x[j] |= a;
      if (t == 3) x[j] ^= a;
    }
    c = (c&x[1]) | (~c&x[0]);
    cout << c << '\n';
  }
}
