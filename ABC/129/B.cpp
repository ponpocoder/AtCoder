#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> w(n), l(n), r(n);
  rep(i, n) cin >> w[i];
  int x = 0;
  rep(i, n) {
    x += w[i];
    l[i] = x;
  }
  int y = 0;
  rep(i, n) {
    r[n-1-i] = y;
    y += w[n-1-i];
  }
  int res = 1001001;
  rep(i, n) res = min(res, abs(l[i]-r[i]));
  cout << res << endl;

}
