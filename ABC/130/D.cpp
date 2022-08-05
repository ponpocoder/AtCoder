#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  ll k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  int r = 0;
  ll res = 0;
  ll curr = 0;
  rep(l, n) {
    while (r < n && curr + a[r] < k) {
      curr += a[r];
      r++;
    }
    res += r - l;
    curr -= a[l];
  }
  res = (ll)(n+1) * n / 2 - res;
  cout << res << endl;
}
