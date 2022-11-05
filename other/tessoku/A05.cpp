#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;
  int res = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <=n; j++) {
    int curr = k - i - j;
    if (curr >= 1 && curr <= n) res += 1;
    }
  }
  cout << res << endl;
}
