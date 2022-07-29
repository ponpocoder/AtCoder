#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int N;
ll dp[3001][3001];
int a[3001];

ll dfs(int l, int r) {
  if (l == r) return a[l];
  if (dp[l][r]) return dp[l][r];
  ll left = a[l] - dfs(l+1, r);
  ll right = a[r] - dfs(l, r-1);
  return dp[l][r] = max(left, right);
}

int main() {
  cin >> N;
  rep(i, N) cin >> a[i];
  cout << dfs(0, N-1) << endl;
}
