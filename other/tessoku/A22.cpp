#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n-1), b(n-1);
  rep(i, n-1) cin >> a[i];
  rep(i, n-1) cin >> b[i];
  vector<int> dp(n, -1001001001);
  dp[0] = 0;
  rep(i, n-1) {
    int x = a[i]-1;
    int y = b[i]-1;
    dp[x] = max(dp[x], dp[i]+100);
    dp[y] = max(dp[y], dp[i]+150);
  }
  cout << dp[n-1] << endl;
}
