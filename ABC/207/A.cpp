#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int res = max(a+b, max(b+c, c+a));
  cout << res << endl;
}
