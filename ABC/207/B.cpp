#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  int res = 0;
  if (c*d > b) {
    res = (a-1)/(c*d-b)+1;
  } else {
    res = -1;
  }
  cout << res << endl;
}
