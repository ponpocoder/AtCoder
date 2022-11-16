#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int h, w;
  cin >> h >> w;
  vector c(h, vector<char>(w));
  rep(i, h) rep(j, w) cin >> c[i][j];
  vector dp(h, vector<ll>(w));
  dp[0][0] = 1;
  rep(i, h) rep(j, w) {
    if (i < h-1 && c[i+1][j] != '#') dp[i+1][j] += dp[i][j];
    if (j < w-1 && c[i][j+1] != '#') dp[i][j+1] += dp[i][j];
  }
  cout << dp[h-1][w-1] << endl;
}
