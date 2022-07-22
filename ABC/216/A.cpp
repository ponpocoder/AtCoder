#include <iostream>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int x, y;
  scanf("%d.%d", &x, &y);
  cout << x;
  if (y <= 2) cout << '-';
  if (7 <= y && y <= 9) cout << '+';
  cout << endl;
}
