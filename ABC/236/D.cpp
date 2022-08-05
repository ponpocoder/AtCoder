#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  int n2 = n*2;
  vector comb(n2, vector<int>(n2, 0));
  rep(i, n2-1) {
    rep(j, n2-1-i) cin >> comb[i][j];
  }
  int n3 = 1 << n2;
  ll res = 0;
  for (int i = 0; i < n3; i++) {
    ll curr = 0;
    for (int j = 0; j < n2; j++) {
      int one = (i >> j) & 1;
      for (int k = j + 1; k < n2; k++) {
        int two = (i >> k) & 1;
        if (one & two) curr ^= comb[i][j];
      }
    }
    res = max(res, curr);
  }

  cout << res << endl;
}
