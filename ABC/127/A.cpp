#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int a, b;
  cin >> a >> b;
  if (a >= 13) cout << b << endl;
  else if (a <= 12 && a >= 6) cout << b/2 << endl;
  else cout << 0 << endl;
}
