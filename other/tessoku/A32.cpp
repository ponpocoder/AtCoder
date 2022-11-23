#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  vector<bool> dp(n+1);
  rep(i, n+1) {
    if (i>=a && !dp[i-a]) dp[i] = true;
    if (i>=b && !dp[i-b]) dp[i] = true;
  }
  if(dp[n]) cout << "First" << endl;
  else cout << "Second" << endl;
}
