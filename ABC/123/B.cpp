#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  vector<int> a(5);
  rep(i, 5) cin >> a[i];
  int d = 0;
  rep(i, 5) {
    int x = 10 - a[i]%10;
    if (x == 10) continue;
    d = max(d, x);
  }
  int s = 0;
  rep(i, 5) {
    int x = 10 - a[i]%10;
    if (x == 10) x = 0;
    s += a[i] + x;
  }
  s -= d;
  cout << s << endl;
}
