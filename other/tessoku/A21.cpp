#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> p(n), a(n);
  rep(i, n) cin >> p[i] >> a[i];

  vector dp(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = n-1; j >= i; j--) {
      int cl = 0, cr = 0;
      if (i > 0 && i <= p[i-1]-1 && p[i-1]-1 <= j) cl = a[i-1];
      if (j < n-1 && i <= p[j+1]-1 && p[j+1]-1 <= j) cr = a[j+1];
      if (i > 0) dp[i][j] = dp[i-1][j] + cl;
      if (j < n-1) dp[i][j] = max(dp[i][j], dp[i][j+1] + cr);
    }
  }
  int res = 0;
  rep(i, n) res = max(res, dp[i][i]);
  cout << res << endl;
}
