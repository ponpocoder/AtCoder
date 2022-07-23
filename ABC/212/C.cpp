#include <iostream>
#include <vector>
using namespace std;

#define rep(i, n) for (int i = 0; i < (n); i++)
const int INF = 1001001001;
int main() {
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(m);
  rep(i, n) cin >> a[i];
  rep(i, m) cin >> b[i];

  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  int i = 0;
  int j = 0;
  int res = INF;
  while (i < n && j < m) {
    int curr = abs(a[i] - b[j]);
    res = min(res, curr);
    if (a[i] < b[j]) i++;
    else j++;
  }
  cout << res << endl;
}
