#include <iostream>
#include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int n, x;
  cin >> n >> x;
  vector<int> a(n);
  rep(i, n) cin >> a[i];

  bool res = false;
  rep(i, n) if (a[i] == x) res = true;
  if (res) cout << "Yes" << endl;
  else cout << "No" << endl;
}
