#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, a, x , y;
  cin >> n >> a >> x >> y;
  int res;
  if (n > a) res = (n-a)*y + x*a;
  else res = x*n;

  cout << res << endl;
}
