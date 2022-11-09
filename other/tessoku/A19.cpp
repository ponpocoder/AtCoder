#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
using P = pair<ll, ll>;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, w;
  cin >> n >> w;
  vector<P> items(n);
  rep(i, n) cin >> items[i].first >> items[i].second;

  vector dp(n+1, vector<ll>(w+1));

  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= w+1; j++) {
      dp[i][j] = max(dp[i][j], dp[i-1][j]);
      if (j - items[i-1].first >= 0) {
        dp[i][j] = max(dp[i][j], dp[i-1][j-items[i-1].first]+items[i-1].second);
      }
    }
  }
  cout << dp[n][w] << endl;
}
