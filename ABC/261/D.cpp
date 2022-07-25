#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> x(n+1);
  rep(i, n) cin >> x[i+1];
  vector<ll> bonus(n+1);
  rep(i, m) {
    int c, y;
    cin >> c >> y;
    bonus[c] += y;
  }

  const ll INF = 1e18;
  vector dp(n+1, vector<ll>(n+1, -INF));
  dp[0][0] = 0;

  for (int i = 1; i <= n; i++) {
    rep(j, n+1) {
      ll now = -INF;
      if (j == 0) {
        rep(k, n+1) now = max(now, dp[i-1][k]);
      } else {
        now = dp[i-1][j-1] + x[i] + bonus[j];
      }
      dp[i][j] = now;
    }
  }
  ll ans = 0;
  rep(i, n+1) ans = max(ans, dp[n][i]);
  cout << ans << endl;
}
