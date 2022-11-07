#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  int r = 0;
  ll res = 0;
  for (int l = 0; l < n; l++) {
    while (r < n && a[r] - a[l] <= k) r++;
    res += r-l-1;
  }
  cout << res << endl;
}

// int main() {
//   int n, k;
//   cin >> n >> k;
//   vector<int> a(n);
//   rep(i, n) cin >> a[i];

//   ll res = 0;
//   rep(i, n) {
//     int l = i;
//     int r = n;

//     while (l + 1 < r) {
//       int m = (l+r) / 2;
//       if (a[m] - a[i] <= k) l = m;
//       else r = m;
//     }
//     // cout << l-i << endl;
//     if (l < n) res += l-i;
//   }
//   cout << res << endl;
// }
