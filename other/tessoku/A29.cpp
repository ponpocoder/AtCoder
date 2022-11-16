#include <iostream>

using namespace std;
using ll = long long;

const int mod = 1000000007;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int powmod(int a, int b) {
  if (b == 0) return 1;
  ll curr = powmod(a, b/2);
  curr *= curr;
  curr %= mod;
  if (b % 2) curr *= a;
  return curr % mod;
}

int main() {
  int a, b;
  cin >> a >> b;
  cout << powmod(a, b) << endl;
}
