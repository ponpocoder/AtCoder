#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int gcd(int a, int b) {
  if (a < b) swap(a, b);
  if (b == 0) return a;
  return gcd(a%b, b);
}

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  vector<int> l(n);
  vector<int> r(n);

  l[0] = a[0];
  for (int i = 1; i < n; i++){
    l[i] = gcd(a[i], l[i-1]);
  }

  r[n-1] = a[n-1];
  for (int i = n-2; i >= 0; i--) {
    r[i] = gcd(a[i], r[i+1]);
  }

  int res = max(l[n-2], r[1]);
  for (int i = 1; i < n-1; i++) {
    res = max(res, gcd(l[i-1], r[i+1]));
  }
  cout << res << endl;
}
