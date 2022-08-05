#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int N, K;
const int mod = 1e9+7;
ll dp[101][100001];
int a[100001];

int main() {
  cin >> N >> K;
  rep(i, N) cin >> a[i];
  for (int i = 0; i < min(K+1, a[0] + 1); i++) dp[0][i] = 1;
  for (int i = 1; i < N; i++) {
    vector<ll> s(K+1, 0);
    s[0] = dp[i-1][0];
    for (int j = 1; j < K + 1; j++) {
      s[j] = s[j-1] + dp[i-1][j];
      s[j] %= mod;
    }
    for (int j = 0; j < K + 1; j++) {
      dp[i][j] += s[j];
      dp[i][j] %= mod;
    }
  }
  int res = 0;
  rep(i, K+1) {res += dp[N][i]; res%= mod;}
  cout << res << endl;
}
