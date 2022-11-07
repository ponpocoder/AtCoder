#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  vector<ll> a(n), b(n), c(n), d(n), p(n*n), q(n*n);
  rep(i, n) cin >> a[i];
  rep(i, n) cin >> b[i];
  rep(i, n) cin >> c[i];
  rep(i, n) cin >> d[i];

  rep(i, n) rep(j, n) {
    p[i*n+j] = a[i] + b[j];
    q[i*n+j] = c[i] + d[j];
  }

  sort(q.begin(), q.end());

  rep(i, n*n) {
    int l = -1;
    int r = n*n;

    while (l <= r) {
      int m = (l+r) / 2;
      ll curr = p[i] + q[m];
      if (curr == k) {
        cout << "Yes" << endl;
        return 0;
      } else if (curr < k) l = m + 1;
      else r = m - 1;
    }
  }
  cout << "No" << endl;
}
