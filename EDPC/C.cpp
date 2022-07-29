#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> dp(3, 0);

  for (int i = 0; i < n; i++){
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> p(3, 0);
    swap(dp, p);
    dp[0] = max(p[1] + b, p[2] + c);
    dp[1] = max(p[0] + a, p[2] + c);
    dp[2] = max(p[0] + a, p[1] + b);
  }
  int res = 0;
  for (int i = 0; i < 3; i++) res = max(res, dp[i]);
  cout << res << endl;
}
