#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

void solve() {
  ll n;
  cin >> n;
  for(ll i = 2;; i++) {
    if (n%i) continue;
    n /= i;
    if (n % i == 0) {
      printf("%lld %lld\n", i, n/i);
      return;
    }
    ll v = round(sqrt(n));
    printf("%lld %lld\n", v, i);
    return;
  }
}

int main() {
  int t;
  cin >> t;
  rep(i, t) solve();
}
