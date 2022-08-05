#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> f(n+1);
  rep(i, n+1) f[i] = i;

  for (int i = 2; i <= n; i++) {
    int x = i * i;
    if (x > n) break;
    for (int j = x; j <= n; j += x) {
      while (f[j]%x == 0) f[j] /= x;
    }
  }
  vector<int> cnt(n+1);
  for (int i = 1; i <= n; i++) {
    cnt[f[i]]++;
  }

  ll res = 0;
  rep(i, n+1) res += (ll)cnt[i] * cnt[i];
  cout << res << endl;
}
