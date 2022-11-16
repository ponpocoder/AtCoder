#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  ll n;
  cin >> n;
  ll x = n / 3;
  ll y = n / 5;
  ll z = n / 15;
  ll res = x + y - z;
  cout << res << endl;
}
