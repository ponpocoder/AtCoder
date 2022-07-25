#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> l(n), r(n);
  for (int i = 0; i < n; i++) {
    int t;
    cin >> t >> l[i] >> r[i];
    l[i] *= 2;
    r[i] *= 2;
    if (t >= 3) l[i]++;
    if (t%2 == 0) r[i]--;
  }
  int res = 0;
  rep(i, n) rep(j, i) {
    if (r[i] < l[j]) continue;
    if (r[j] < l[i]) continue;
    res++;
  }
  cout << res << endl;
}
