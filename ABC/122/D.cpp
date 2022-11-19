#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

const int mod = 1000000007;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  vector dp(n+1, vector<vector<vector<int>>>(4, vector<vector<int>>(4, vector<int>(4))));
  // dp[i][j][k][l]: i番目の数字を見て最後1,2,3文字目がそれぞれj,k,lである時の場合の数
  dp[0][0][0][0] = 1;
  rep(i, n) {
    rep(j, 4) {
      rep(k, 4) {
        rep(l, 4) {
          rep(x, 4) {
            if (x == 2 && j == 1 && k == 0) continue;
            if (x == 1 && j == 2 && k == 0) continue;
            if (x == 2 && j == 0 && k == 1) continue;
            if (x == 2 && j == 1 && l == 0) continue;
            if (x == 2 && k == 1 && l == 0) continue;

            dp[i+1][x][j][k] += dp[i][j][k][l];
            dp[i+1][x][j][k] %= mod;
          }
        }
      }
    }
  }
  int res = 0;
  rep(j, 4) {
    rep(k, 4) {
      rep(l, 4) {
        res += dp[n][j][k][l];
        res %= mod;
      }
    }
  }
  cout << res << endl;
}
