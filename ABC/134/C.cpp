#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)
int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  vector<int> s = a;
  sort(s.rbegin(), s.rend());
  rep(i, n) {
    int res = s[0];
    if (s[0] == a[i]) res = s[1];
    cout << res << endl;
  }
}
