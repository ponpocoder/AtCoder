#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int n, k;
vector<int> a(100);
vector<int> dp(100001);

bool dfs(int k) {
  if (dp[k] != -1) return dp[k];
  for (int j = 0; j < n; j++) {
    if (k < a[j]) continue;
    if (!dfs(k-a[j])) return dp[k] = 1;
  }
  return dp[k] = 0;
}

int main() {
  cin >> n >> k;
  rep(i, n) cin >> a[i];
  rep(i, k+1) dp[i] = -1;
  dp[0] = 0;
  if (dfs(k)) cout << "First" << endl;
  else cout << "Second" << endl;
}
