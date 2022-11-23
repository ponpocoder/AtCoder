#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, m, b;
  cin >> n >> m >> b;
  int x = 0, y = 0;
  rep(i, n) {
    int v;
    cin >> v;
    x += v;
  }
  rep(i, m) {
    int v;
    cin >> v;
    y += v;
  }
  ll res = (ll)x*m+(ll)y*n+(ll)b*n*m;
  cout << res << endl;
}
