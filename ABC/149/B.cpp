#include <iostream>
#include <algorithm>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  ll a, b, k;
  cin >> a >> b >> k;
  ll tmp = a;
  a = max((ll)0, a-k);
  k = max((ll)0, k-tmp);
  b = max((ll)0, b-k);
  cout << a << " " << b << endl;
}
