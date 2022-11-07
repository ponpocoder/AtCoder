#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int n, k;

bool check(ll x, vector<int> a) {
  ll s = 0;
  rep(i, n) s += x / a[i];
  return s >= k;
}

int main() {
  cin >> n >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int l = 1;
  int r = 1001001001;
  while (l +1 < r) {
    ll m = (l + r) / 2;
    if (check(m, a)) r = m;
    else l = m;
  }
  cout << r << endl;
}
