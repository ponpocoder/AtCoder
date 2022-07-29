#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int N, W;
  cin >> N >> W;
  vector<int> w(N), v(N);
  const int V = 100001;
  vector dp(N+1, vector<ll>(V, W+1));
  dp[0][0] = 0;
  rep(i, N)  cin >> w[i] >> v[i];
  for (int i = 1; i < N+1; i++) {
    for (int j = 0; j < V; j++) {
      if (j - v[i-1] >= 0) dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]] + w[i-1]);
      else dp[i][j] = dp[i-1][j];
    }
  }

  int res = 0;
  for (int i = V - 1; i >= 0; i--) if (dp[N][i] <= W) { res = i; break;}
  cout << res << endl;
}
