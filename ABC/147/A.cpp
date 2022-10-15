#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int a, b, c;
  cin >> a >> b >> c;
  int s = a + b + c;
  if (s >= 22) cout << "bust" << endl;
  else cout << "win" << endl;
}
