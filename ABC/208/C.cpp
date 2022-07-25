#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n; ll k;
  cin >> n >> k;
  vector<int> a(n);
  map<ll, ll> f, g;
  rep(i, n) {
    cin >> a[i];
    f[i] = a[i];
    g[a[i]] = i;
  }

  vector<ll> res(n, 0);
  if (k >= n) {
    ll curr = k / n;
    rep(i, n) res[i] += curr;
    k %= n;
  }
  //cout << k << endl;
  sort(a.begin(), a.end());
  for (ll i = 0; i < k; i++) {
    res[g[a[i]]] += 1;
  }

  rep(i, n) cout << res[i] << endl;
}
