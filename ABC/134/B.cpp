#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, d;
  cin >> n >> d;
  int x = 1 + 2*d;
  int res = (n+x-1)/x;
  cout << res << endl;
}
