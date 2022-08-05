#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
const int mod = 998244353;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n), b(n);
  rep(i, n) cin >> a[i];
  rep(i, n) cin >> b[i];
  int m = 3001;
  vector<int> dp(m);
  dp[0] = 1;
  rep(i, n) {
    vector<int> p(m);
    swap(dp, p);
    rep(j, m-1) {
      p[j+1] += p[j];
      p[j+1] %= mod;
    }
    rep(j, m) {
      if (a[i] <= j && j <= b[i]) {
        dp[j] += p[j];
        dp[j] %= mod;
      }
    }
  }
  int res = 0;
  rep(i, m) { res += dp[i]; res %= mod;}
  cout << res << endl;
}
