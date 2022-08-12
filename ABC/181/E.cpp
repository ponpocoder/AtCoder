#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> h(n);
  vector<int> w(m);
  rep(i, n) cin >> h[i];
  rep(i, n) cin >> w[i];
  sort(h.begin(), h.end());
  vector<int> diff(n, 0);
  for (int i = 0; i < n; i++) {
    if (i % 2) continue;
    diff[i] = h[i] - h[i-1];
  }

}
