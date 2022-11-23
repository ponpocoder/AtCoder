#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> a(n+1);
  rep(i, n+1) a[i] = i;
  bool reverse = false;
  rep(i, q) {
    int v;
    cin >> v;
    if (v == 1) {
      int x, y;
      cin >> x >> y;
      if (reverse) a[n+1-x] = y;
      else a[x] = y;
    } else if (v == 2) reverse ^= 1;
    else {
      int x;
      cin >> x;
      if (reverse) cout << a[n+1-x] << endl;
      else cout << a[x] << endl;
    }
  }
}
