#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, q;
  cin >> n >> q;
  vector<int> a(n), s(n+1);
  rep(i, n) cin >> a[i];
  rep(i, n) s[i+1] += a[i] + s[i];

  rep(i, q) {
    int l, r;
    cin >> l >> r;
    int res = s[r] - s[l-1];
    cout << res << endl;
  }
}
