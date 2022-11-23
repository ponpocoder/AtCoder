#include <iostream>
#include <vector>
#include <set>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)
const int INF = 1001001001;

int main() {
  int n, m;
  cin >> n >> m;
  vector a(m, vector<int>(n));
  rep(i, m) rep(j, n) cin >> a[i][j];
  int n2 = 1 << n;
  vector dp(n+1, vector<int>(n2, INF));
  // i種類目の品物までみて、状態jのときのクーポンの最小使用枚数
  dp[0][0] = 0;
  rep(i, n) {
    rep(j, n2) {
      if (i > 0) dp[i][j] = min(dp[i][j], dp[i-1][j]);
      if (dp[i][j] == INF) continue;
      rep(k, m) {
        int nj = j;
        rep(l, n) nj |= a[k][l]<<(n-1-l);
        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j]+1);
      }
    }
  }
  int res = dp[n][n2-1];
  if (res == INF) res = -1;
  cout << res << endl;
}
