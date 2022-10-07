#include <iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int x = 0;
  int y = 0;
  for (int i = 0; i < b; i++) {
    x *= 10;
    x += a;
  }
  for (int i = 0; i < a; i++) {
    y *= 10;
    y += b;
  }
  if (x < y) cout << x << endl;
  else cout << y << endl;
}
