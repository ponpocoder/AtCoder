#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int p, q, r;
  cin >> p >> q >> r;
  int res = min({p+q, q+r, r+p});
  cout << res << endl;
}
