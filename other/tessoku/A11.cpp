#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for(int i = 0; i < n; i++)

int main() {
  int n, x;
  cin >> n >> x;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  int l = 0, r = n;
  while (l + 1 < r) {
    int m = (l+r) / 2;
    if (a[m] == x) {
      cout << m+1 << endl;
      return 0;
    } else if (a[m] > x) {
      r = m;
    } else {
      l = m;
    }
  }
}
