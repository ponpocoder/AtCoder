#include <iostream>
#include <iomanip>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

double dp[3000][3000];
double p[3000];

int main() {
  int n;
  cin >> n;
  rep(i, n) cin >> p[i];
  dp[0][0] = 1;
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j <= i; j++) {
      if (j != 0) dp[i][j] += dp[i-1][j-1] * p[i-1];
      dp[i][j] += dp[i-1][j] * (1 - p[i-1]);
    }
  }
  double res = 0;
  //rep(i, n+1) cout << dp[n][i] << endl;
  for (int i = n/2+1; i <= n; i++) res += dp[n][i];
  cout << fixed << setprecision(9) << res << endl;
}
