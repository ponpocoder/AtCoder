#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n), l(n+1), r(n+1);
  rep(i, n) cin >> a[i];
  for (int i = 0; i < n; i++) {
    l[i+1] = max(l[i], a[i]);
  }
  for (int i = n; i >= 1; i--) {
    r[i-1] = max(r[i], a[i-1]);
  }
  int d;
  cin >> d;
  rep(i, d) {
    int x, y;
    cin >> x >> y;
    int res = max(l[x-1], r[y]);
    cout << res << endl;
  }
}
