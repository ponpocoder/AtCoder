#include <iostream>

using namespace std;
using ll = long long;

const int mod = 1000000007;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int factorial(int x) {
  if (x == 0) return 1;
  ll curr = (ll)x * factorial(x-1);
  return curr % mod;
}

int powmod(int a, int b) {
  if(b == 0) return 1;
  ll curr = powmod(a, b/2);
  curr *= curr;
  curr %= mod;
  if (b % 2) curr *= a;
  return curr % mod;
}

int main() {
  int n, r;
  cin >> n >> r;
  ll curr = factorial(n);
  int x = powmod(factorial(r), mod-2);
  int y = powmod(factorial(n-r), mod-2);
  // cout << curr << " " << x << " " << y << endl;
  curr *= x;
  curr %= mod;
  curr *= y;
  curr %= mod;
  cout << curr << endl;
}
