#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, x;
  cin >> n >> x;
  vector<int> l(n);
  rep(i, n) cin >> l[i];
  int curr = 0;
  int cnt = 0;
  rep(i, n) {
    if (curr > x) break;
    cnt += 1;
    curr += l[i];
  }
  if (curr <= x) cnt += 1;
  cout << cnt << endl;
}
