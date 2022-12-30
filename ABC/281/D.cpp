#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T b) { return a < b ? a = b, true: false; }

int main() {
  int n, k, d;
  cin >> n >> k >> d;
  vector<ll> a(n);
  rep(i, n) cin >> a[i];
  // i番目まで見て今j個選んでいて和割るdの余りがrのときの和の最大値
  vector dp(n+1, vector<vector<ll>>(k+1, vector<ll>(d+1, -1)));
  dp[0][0][0] = 0;
  rep(i, n)rep(j, k+1)rep(r, d) {
      ll curr = dp[i][j][r];
      if (curr == -1) continue;
      chmax(dp[i+1][j][r], curr);
      if (j == k) continue;
      chmax(dp[i+1][j+1][(r+a[i])%d], curr+a[i]);
  }
  cout << dp[n][k][0] << endl;
}
