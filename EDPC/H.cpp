#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
const int mod = 1e9+7;

#define rep(i, n) for (int i = 0; i < (n); i++)

int h, w;
char grid[1001][1001];
ll dp[1001][1001];

int dfs(int i, int j) {
  if (i < 0 || j < 0 || i >= h || j >= w || grid[i][j] == '#') return 0;
  if (dp[i][j] != -1) return dp[i][j];
  dp[i][j] = dfs(i-1, j) + dfs(i, j-1);
  dp[i][j] %= mod;
  return dp[i][j];
}

int main() {
  cin >> h >> w;
  rep(i, h) rep(j, w) cin >> grid[i][j];
  rep(i, h) rep(j, w) dp[i][j] = -1;
  dp[0][0] = 1;
  cout << dfs(h-1, w-1) << endl;
}
