#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int n, k, m;
  int curr = 0;
  cin >> n >> k >> m;
  vector<int> a(n);
  rep(i, n-1) cin >> a[i];
  rep(i, n-1) curr += a[i];
  int remain = n * m - curr;
  remain = max(remain, 0);
  if (remain > k) {
    cout << -1 << endl;
  } else {
    cout << remain << endl;
  }
}
