#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, s;
  cin >> n >> s;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  vector dp(n+1, vector<bool>(600001));
  dp[0][0] = true;
  rep(i, n) rep(j, 600001) {
    if (i >= 1 && dp[i-1][j]) dp[i][j] = true;
    if (!dp[i][j]) continue;
    if (a[i] + j < 6000001) dp[i+1][a[i]+j] = true;
  }
  rep(i, n+1) {
    if (dp[i][s]) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  cout << "No" << endl;
}
