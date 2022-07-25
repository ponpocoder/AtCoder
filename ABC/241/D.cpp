#include <iostream>
#include <set>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int q;
  cin >> q;
  multiset<ll> s;
  for (int i = 0; i < q; i++) {
    int t; ll x;
    cin >> t >> x;
    if (t == 1) {
      s.insert(x);
    } else {
      int k;
      cin >> k;
      ll res = -1;
      if (t == 2) {
        auto it = s.upper_bound(x);
        bool ok = true;
        for (int j = 0; j < k; j++) {
          if (it == s.begin()) {
            ok = false;
            break;
          }
          it--;
        }
        if (ok) res = *it;
      } else {
        auto it = s.lower_bound(x);
        bool ok = true;
        for (int j = 0; j < k - 1; j++) {
          if (it == s.end()) {
            ok = false;
            break;
          }
          it++;
        }
        if (ok && it != s.end()) res = *it;
      }

      cout << res << '\n';
    }
  }
}
