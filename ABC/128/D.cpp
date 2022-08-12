#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  rep(i, n) cin >> v[i];
  int res = 0;

  for (int l = 0; l <= k; l++) {
    for (int r = 0; r <= k - l; r++) {
      if (l+r > n) break;
      int d = k - (l + r);
      int curr = 0;
      vector<int> b;
      rep(i, l) b.push_back(v[i]);
      rep(i, r) b.push_back(v[n-1-i]);

      int x = b.size();
      rep(i, x) curr += b[i];

      sort(b.begin(), b.end());
      rep(i, min(d, x)) {
        if (b[i] >= 0) break;
        curr -= b[i];
      }
      res = max(res, curr);
    }
  }
  cout << res <<endl;
}
