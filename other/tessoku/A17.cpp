#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n-1), b(n-2), s(n), res;
  rep(i, n-1) cin >> a[i];
  rep(i, n-2) cin >> b[i];

  for (int i = 1; i < n; i++) {
    s[i] = s[i-1] + a[i-1];
    if (i >= 2) s[i] = min(s[i], s[i-2] + b[i-2]);
  }
  int curr = n-1;
  while (curr >= 0) {
    res.push_back(curr);
    if (s[curr-1] + a[curr-1] == s[curr]) curr -=1;
    else curr -= 2;
  }
  reverse(res.begin(), res.end());
  cout << res.size() << endl;
  rep(i, res.size()) {
    if (i > 0) cout << " ";
    cout << res[i]+1;
  }
  cout << endl;
}
