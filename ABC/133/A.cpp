#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  int res = min(n*a, b);
  cout << res << endl;
}
