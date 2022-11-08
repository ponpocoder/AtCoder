#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n;
  cin >> n;
  vector<int> a(n-1), b(n-2), s(n);
  rep(i, n-1) cin >> a[i];
  rep(i, n-2) cin >> b[i];

  for (int i = 1; i < n; i++) {
    int curr = s[i-1] + a[i-1];
    if (i >= 2) curr = min(curr, s[i-2]+b[i-2]);
    s[i] = curr;
  }
  cout << s[n-1] << endl;


}
