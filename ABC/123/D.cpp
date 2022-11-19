#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int x, y, z, k;
  cin >> x >> y >> z >> k;
  vector<ll> a(x), b(y), c(z), res;
  rep(i, x) cin >> a[i];
  rep(i, y) cin >> b[i];
  rep(i, z) cin >> c[i];

  sort(a.rbegin(), a.rend());
  sort(b.rbegin(), b.rend());
  sort(c.rbegin(), c.rend());

  rep(i, x) {
    rep(j, y) {
      if((i+1)*(j+1) > k) break;
      rep(l, z) {
        if ((i+1)*(j+1)*(l+1) > k) break;
        res.push_back(a[i]+b[j]+c[l]);
      }
    }
  }
  sort(res.rbegin(), res.rend());
  rep(i, k) cout << res[i] << endl;
}
