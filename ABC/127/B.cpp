#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int r, d, x;
  cin >> r >> d >> x;
  rep(i, 10) {
    x = r * x - d;
    cout << x << endl;
  }
}
